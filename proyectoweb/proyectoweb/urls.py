from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('proyectowebapp.urls')),
    path('blog/',include('blog.urls')),
    path('', include('tienda.urls')),
    path('carro/', include('carro.urls')),
    path('autenticacion/', include('autenticacion.urls')), #Redireccionar el carrito.
    path('pedidos/', include('pedidos.urls')),
]
