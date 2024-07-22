from django.shortcuts import render, redirect
from pedidos.models import  Pedidos,LineaPedido
from carro.carro import Carro
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.html import strip_tags
from django.template.loader import render_to_string
from django.core.mail import send_mail
from tienda.models import Producto


@login_required(login_url="/Autenticacion/loguear")

def procesar_pedidos(request):
    pedido = Pedidos.objects.create(user = request.user)
    carro = Carro(request)
    lineas_pedidos = list()
    for key, value in carro.carro.items():
        producto_id = key
        cantidad = value["cantidad"]
        producto = Producto.objects.get(id = producto_id)
        lineas_pedidos.append(LineaPedido(
            producto = producto,
            cantidad = cantidad,
            user = request.user,
            pedido = pedido,
        
        ))

    LineaPedido.objects.bulk_create(lineas_pedidos)
    total_pedido = pedido.total
  


    enviar_email(
        pedido = pedido, 
        lineas_pedidos = lineas_pedidos,
        nombre_usuario = request.user.username,
        email_usuario = request.user.email,
        total = total_pedido,
    )

    messages.success(request, "Datos almacenados correctamente, el pedido esta hecho")
    return redirect("../tienda")

def enviar_email(**kwargs):
    asunto = "Muchas gracias por el pedido"
    mensaje = render_to_string("emails/pedido.html", {
        "pedido": kwargs.get("pedido"),
        "lineas_pedidos": kwargs.get("lineas_pedidos"),
        "nombre_usuario": kwargs.get("nombre_usuario"),
        "email_usuario": kwargs.get("email_usuario"),
        "total": kwargs.get("total")
    })
    mensaje_texto = strip_tags(mensaje)
    from_email = "webstorewarriors@gmail.com"
    to = kwargs.get("email_usuario")
    #to = "felipeq627@gmail.com"

    send_mail(asunto, mensaje_texto, from_email, [to], html_message=mensaje)