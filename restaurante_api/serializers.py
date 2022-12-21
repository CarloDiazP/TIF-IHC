from rest_framework import serializers
from inicio.models import Pedido, Mesa, Carrito, Cliente, Factura, Producto

class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = ["id_mesa", "fecha", "estado", "total_productos", "delivery"]

class MesaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mesa
        fields = ["nombre_mesa", "disponibilidad"]

class CarritoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrito
        fields = ["id_pedido", "cantidad", "precio_total"]

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ["dni", "nombre", "pApellido", "sApellido", "mail", "direccion", "opinion", "contrasena", "esAutenticado"]

class FacturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Factura
        fields = ["id_pedido", "id_cliente", "fecha", "modo_pagar", "total_factura"]

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ["nombre", "categoria", "tipo", "precio", "disponible", "imagen"]