from django.db import models
from django.utils import timezone

# Create your models here.
class Pedido(models.Model):
  COCINANDO = 1
  LISTO = 2
  EN_CAMINO = 3
  ENTREGADO = 4

  ESTADOS = (
    (COCINANDO, "Cocinando"),
    (LISTO, "Listo"),
    (EN_CAMINO, "En camino"),
    (ENTREGADO, "Entregado"),
  )

  id_mesa = models.IntegerField()
  fecha = models.DateTimeField(default=timezone.now)
  estado = models.IntegerField(choices=ESTADOS, default=1)
  total_productos = models.IntegerField()
  delivery = models.BooleanField()

class Cliente(models.Model):
  dni = models.CharField(max_length=9)
  nombre = models.CharField(max_length=100)
  pApellido = models.CharField(max_length=100)
  sApellido = models.CharField(max_length=100)
  mail = models.EmailField(max_length = 254)
  direccion = models.CharField(max_length=100)
  opinion = models.TextField(default=" ")
  contrasena = models.CharField(max_length=100, default="qwerty123")
  esAutenticado = models.BooleanField(default=True)

class Carrito(models.Model):
  id_pedido = models.IntegerField()
  id_productos = models.IntegerField()
  cantidad = models.IntegerField()
  precio_total = models.IntegerField()

class Producto(models.Model):
  COMIDA = 1
  POSTRE = 2
  BEBIDA = 3
  ENTRADA = 4

  CATEGORIAS = (
    (COMIDA, "Comida"),
    (POSTRE, "Postre"),
    (BEBIDA, "Bebida"),
    (ENTRADA, "Entrada"),
  )

  nombre = models.CharField(max_length=100)
  categoria = models.IntegerField(choices=CATEGORIAS)
  tipo = models.CharField(max_length=100)
  precio = models.IntegerField()
  disponible = models.BooleanField()
  imagen = models.TextField()

class Factura(models.Model):
  TARJETA = 1
  EFECTIVO = 2

  MODOS_PAGO = (
    (TARJETA, "Tarjeta"),
    (EFECTIVO, "Efectivo"),
  )

  id_pedido = models.IntegerField()
  id_cliente = models.IntegerField()
  fecha = models.DateTimeField(default=timezone.now)
  modo_pagar = models.IntegerField(choices=MODOS_PAGO)
  total_factura = models.IntegerField()

class Mesa(models.Model):
  nombre_mesa = models.CharField(max_length=100)
  disponibilidad = models.BooleanField()