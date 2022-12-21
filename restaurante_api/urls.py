from django.urls import path, include
from .views import (
    PedidoListApiView,
    MesaListApiView,
    CarritoListApiView,
    ClienteListApiView,
    FacturaListApiView,
    ProductoListApiView,
)
# Pedido, Mesa, Carrito, Cliente, Factura, Producto

urlpatterns = [
    path('api-pedido', PedidoListApiView.as_view()),
    path('api-mesa', MesaListApiView.as_view()),
    path('api-carrito', CarritoListApiView.as_view()),
    path('api-cliente', ClienteListApiView.as_view()),
    path('api-factura', FacturaListApiView.as_view()),
    path('api-producto', ProductoListApiView.as_view()),
]