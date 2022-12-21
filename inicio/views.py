from ast import And
from django.shortcuts import render
from django.http import HttpResponse
from .models import Pedido, Mesa, Carrito, Cliente, Factura, Producto
from django.shortcuts import redirect
from django.contrib import messages


# from .models import Producto
# from .models import Cliente

# Create your views here.
def myHomeView(request, *args, **kwargs):
    if request.method == 'POST':
        contrasena = request.POST['contrasena']
        mail = request.POST['mail']
        cliente1 = Cliente.objects.get(contrasena=contrasena)
        cliente2 = Cliente.objects.get(mail=mail)
        print(cliente1.id)
        print(cliente2.id)
        if cliente1.id == cliente2.id:
            nombre = cliente2.nombre
            esAutenticado = 1
    elif request.method == 'GET':
        nombre = "NoDefinido"
        esAutenticado = 0
            
    print(nombre)
    print(esAutenticado)
    producto = Producto.objects.all()
    cliente = Cliente.objects.all()
    mesas = Mesa.objects.all()
    # print(args, kwargs)
    # print(request.user)
    return render(request, "index.html", {'productos': producto, 'clientes': cliente, 'esAutenticado': esAutenticado, 'nombre': nombre, 'mesas': mesas})

def myShoppingView(request, *args, **kwargs):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        mail = request.POST['mail']
        descripcion = request.POST['descripcion']
        servicio = request.POST['servicio']
        productos = descripcion.replace("\r", "").split("\n")
        productos = productos[:-1]
        print(productos)
        try:
            cliente1 = Cliente.objects.get(nombre=nombre).id
            cliente2 = Cliente.objects.get(mail=mail).id
        except:
            cliente1 = 1
            cliente2 = 2
        id_mesa = -1
        if cliente1 == cliente2:
            estado = 1
            delivery = False
            if servicio == 'Delivery':
                delivery = True
            else:
                id_mesa = Mesa.objects.get(nombre_mesa=servicio).id

            Pedido.objects.create(id_mesa=id_mesa, estado=estado, total_productos=len(productos), delivery=delivery)
        else:
            messages.error(request, 'Cuenta no válida')
            return redirect('/')
        list_productos = []
        precio_total = 0
        for producto in productos:
            p = Producto.objects.get(nombre=producto)
            precio_total = precio_total + p.precio
            list_productos.append(p)
    elif request.method == 'GET':
        print("metodo get")
    return render(request, "carrito.html", {'productos': list_productos, 'esAutenticado': True, 'nombre': nombre, 'precio_total': precio_total, 'servicio': servicio})

def myLoginView(request, *args, **kwargs):
    print(request.GET)
    return render(request, "iniciar-sesion.html", {'esAutenticado': False})

def myRegisterView(request, *args, **kwargs):
    return render(request, "registrarse.html", {'esAutenticado': False})
