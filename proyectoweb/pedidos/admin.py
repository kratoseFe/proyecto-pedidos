from django.contrib import admin
from .models import Pedidos, LineaPedido

admin.site.register([Pedidos, LineaPedido])
