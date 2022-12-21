from django.contrib import admin
from .models import Pedido, Mesa, Carrito, Cliente, Factura, Producto

# Register your models here.

admin.site.register(Pedido)
admin.site.register(Mesa)
admin.site.register(Carrito)
admin.site.register(Cliente)
admin.site.register(Factura)
admin.site.register(Producto)
