from django.shortcuts import render, redirect
from django.views.generic import View, CreateView #Para cargar las vistas genéricas que me ofrece Django
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm #Creación del usuario y ya creado el usuario hacer la autenticación
from django.contrib.auth import login, logout, authenticate #Permite hacer el logueo de la tabla autenticación
from django.contrib import messages #Permite cargar la librería de mensajes django para errores
from .forms import UserCreationformWhithEmail


""" def autenticacion(request):
    return render(request, 'registro/registro.html') """

class VRegistro(View): #Inicialización de una clase vista para el registro
    def get(self, request): #Metodo para get
        form = UserCreationformWhithEmail #Variable que me permite la creación del formulario
        return render(request, 'registro/registro.html', {'form': form}) #Retorna el archivo renderizado del registro.html y el formulario con sus campos
    
    def post(self, request):
        form = UserCreationformWhithEmail(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            messages.success(request, "Usuario Registrado")
            return redirect('home')
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
        return render(request, 'registro/registro.html', {'form': form})
    
def cerrar_sesion(request):
    logout(request)
    return redirect('home')

def loguear(request):
    if request.method =='POST':
        form = AuthenticationForm(request, data = request.POST) #Permite capturar las datos que están en el formulario de logueo
        if form.is_valid():
            nombre_usuario = form.cleaned_data.get('username')
            contrasena = form.cleaned_data.get('password')
            usuario = authenticate(username = nombre_usuario, password = contrasena)
            if usuario is not None: 
                login(request, usuario)
                return redirect('home')
            else:
                messages.error(request, 'El usuario no se encuentra en la base de datos :[')

        else:
            messages.error(request, 'Lo sentimos, al parecer la información está incorrecta :[')        
                
    form = AuthenticationForm()
    return render(request, 'login/login.html', {'form': form})
