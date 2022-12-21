from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from inicio.models import Pedido, Mesa, Carrito, Cliente, Factura, Producto
from .serializers import PedidoSerializer, MesaSerializer, CarritoSerializer, ClienteSerializer, FacturaSerializer, ProductoSerializer
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages

class PedidoListApiView(APIView):
    # add permission to check if user is authenticated
    # permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''
        pedidos = Pedido.objects.all()
        serializer = PedidoSerializer(pedidos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Todo with given todo data
        '''
        # ["id_mesa", "fecha", "estado", "total_productos", "delivery"]
        data = {
            'id_mesa': request.data.get('id_mesa'), 
            'fecha': request.data.get('fecha'),
            'estado': request.data.get('estado'),
            'total_productos': request.data.get('total_productos'),
            'delivery': request.data.get('delivery'),
        }
        serializer = PedidoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MesaListApiView(APIView):
    # add permission to check if user is authenticated
    # permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''
        mesas = Mesa.objects.all()
        serializer = MesaSerializer(mesas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Todo with given todo data
        '''
        # ["nombre_mesa", "disponibilidad"]
        data = {
            'nombre_mesa': request.data.get('nombre_mesa'), 
            'disponibilidad': request.data.get('disponibilidad'), 
        }
        serializer = MesaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CarritoListApiView(APIView):
    # add permission to check if user is authenticated
    # permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''
        carritos = Carrito.objects.all()
        serializer = CarritoSerializer(carritos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Todo with given todo data
        '''
        # ["id_pedido", "cantidad", "precio_total"]
        data = {
            'id_pedido': request.data.get('id_pedido'), 
            'cantidad': request.data.get('cantidad'), 
            'precio_total': request.data.get('precio_total'), 
        }
        serializer = CarritoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            # return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ClienteListApiView(APIView):
    # add permission to check if user is authenticated
    # permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''
        clientes = Cliente.objects.all()
        serializer = ClienteSerializer(clientes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Todo with given todo data
        '''
        # ["dni", "nombre", "pApellido", "sApellido", "mail", "direccion", "opinion"]
        data = {
            'dni': request.data.get('dni'), 
            'nombre': request.data.get('nombre'), 
            'pApellido': request.data.get('pApellido'), 
            'sApellido': request.data.get('sApellido'), 
            'mail': request.data.get('mail'), 
            'direccion': request.data.get('direccion'), 
            'opinion': request.data.get('opinion'), 
            'contrasena': request.data.get('contrasena'), 
            #'esAutenticado': request.data.get('esAutenticado'), 
        }
        serializer = ClienteSerializer(data=data)
        if serializer.is_valid():
            dni = request.POST["dni"]
            nombre = request.POST["nombre"]
            mail = request.POST["mail"]
            if not len(dni) == 8:
                messages.error(request, 'DNI inválido')
                return redirect('/registrarse/')
            elif Cliente.objects.filter(nombre=nombre).exists():
                messages.error(request, 'El nombre ya está tomado')
                return redirect('/registrarse/')
            elif Cliente.objects.filter(mail=mail).exists():
                messages.error(request, 'Ya se creó una cuenta con este email')
                return redirect('/registrarse/')
            # producto = Producto.objects.all()
            # cliente = Cliente.objects.all()
            serializer.save()
            return redirect("/iniciar-sesion")
            # return render(request, "index.html", {'productos': producto, 'clientes': cliente, 'esAutenticado': True})
            # return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FacturaListApiView(APIView):
    # add permission to check if user is authenticated
    # permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''
        facturas = Factura.objects.all()
        serializer = FacturaSerializer(facturas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Todo with given todo data
        '''
        # ["id_pedido", "id_cliente", "fecha", "modo_pagar", "total_factura"]
        data = {
            'id_pedido': request.data.get('id_pedido'), 
            'id_cliente': request.data.get('id_cliente'), 
            'fecha': request.data.get('fecha'), 
            'modo_pagar': request.data.get('modo_pagar'), 
            'total_factura': request.data.get('total_factura'),
        }
        serializer = FacturaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductoListApiView(APIView):
    # add permission to check if user is authenticated
    # permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''
        productos = Producto.objects.all()
        serializer = ProductoSerializer(productos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Todo with given todo data
        '''
        # ["nombre", "categoria", "tipo", "precio", "disponible", "imagen"]      
        data = {
            'nombre': request.data.get('nombre'), 
            'categoria': request.data.get('categoria'), 
            'tipo': request.data.get('tipo'),
            'precio': request.data.get('precio'), 
            'disponible': request.data.get('disponible'), 
            'imagen': request.data.get('imagen'),
        }
        serializer = ProductoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
