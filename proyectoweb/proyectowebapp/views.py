from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import send_mail
from carro.carro import Carro
from servicios.models import Servicios, Contacto
from proyectoweb.forms import FormularioContacto
from django.core.mail import EmailMessage
from django.core.paginator import Paginator


def home (request):
    carro = Carro(request)
    return render(request, "home.html", {})

def servicios (request):
    listado = Servicios.objects.all()
    paginator = Paginator(listado, 1)
    pagina = request.GET.get("page") or 1
    lista = paginator.get_page(pagina)
    pagina_actual = int(pagina)
    paginas = range(1, lista.paginator.num_pages + 1) 
    return render(request, "servicio.html", {'servicios':lista, 'paginas':paginas, 'pagina_actual': pagina_actual})

# def tienda (request):
#     return render(request, "tienda.html", {})

# def blog (request):
#     return render(request, "blog.html", {})

#-----------------------------------------------------------------------------------------------------------------------------#
# Fragmento de código para el envío de correos de contacto
#def contacto(request):
    # if request.method=="POST":
    #     subject = request.POST["asunto"]
    #     name = request.POST["usuario"]
    #     message = request.POST["mensaje"] + "  A nombre de " + name + " " + request.POST["email"]
    #     email_from = settings.EMAIL_HOST_USER
    #     recipient_list = ["webstorewarriors@gmail.com"]
    #     send_mail(subject, message, email_from, recipient_list)

    #     return HttpResponse("<h1>Gracias por enviar<h1/>")
    # return render(request, 'contacto.html')
#-----------------------------------------------------------------------------------------------------------------------------#

def contacto(request):
    formulario = FormularioContacto()#Creo variable formulario que me contendrá todos los valores del formulario creado en forms.py
    if request.method=='POST': #Evalúo si el metodo es POST verificable en contacto.html
        formulario=FormularioContacto(data=request.POST)#Captura datos del formulario, Nombre, Email, Contenido
        if formulario.is_valid():
            nombre = request.POST.get('nombre')
            email = request.POST.get('email')
            contenido = request.POST.get('contenido')
            email = EmailMessage("App Gestión de Pedidos Warriors",
                                 "El usuario {} con Email {} envió el siguiente asunto \n\n{}".format(nombre, email, contenido),
                                 "", ["webstorewarriors@gmail.com"], reply_to=[email])
            try:
                email.send()
                return redirect('/contacto/?valido')
            except:
                return redirect('/contacto/?invalido')
            
    return render(request, 'contacto.html', {'miFormulario':formulario})

def mostrarcontacto (request):
    lista=Contacto.objects.all()
    return render (request,"mostrar_contacto.html",{'contacto':lista})