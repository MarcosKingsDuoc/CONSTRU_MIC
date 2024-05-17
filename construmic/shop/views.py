from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Producto, Carrito, CarritoProducto, Pedido, PedidoProducto

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'lista_productos.html', {'productos': productos})

def detalle_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    return render(request, 'detalle_producto.html', {'producto': producto})

@login_required
def agregar_al_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    carrito, creado = Carrito.objects.get_or_create(usuario=request.user)
    carrito_producto, creado = CarritoProducto.objects.get_or_create(carrito=carrito, producto=producto)
    if not creado:
        carrito_producto.cantidad += 1
        carrito_producto.save()
    return redirect('carrito')

@login_required
def ver_carrito(request):
    carrito, creado = Carrito.objects.get_or_create(usuario=request.user)
    productos_en_carrito = CarritoProducto.objects.filter(carrito=carrito)
    total = sum(item.producto.precio * item.cantidad for item in productos_en_carrito)
    return render(request, 'ver_carrito.html', {'productos_en_carrito': productos_en_carrito, 'total': total})

@login_required
def comprar(request):
    carrito = get_object_or_404(Carrito, usuario=request.user)
    productos_en_carrito = CarritoProducto.objects.filter(carrito=carrito)
    
    if not productos_en_carrito.exists():
        return redirect('carrito')
    
    total = sum(item.producto.precio * item.cantidad for item in productos_en_carrito)
    pedido = Pedido.objects.create(usuario=request.user, total=total, fecha=timezone.now())
    
    for item in productos_en_carrito:
        PedidoProducto.objects.create(
            pedido=pedido,
            producto=item.producto,
            cantidad=item.cantidad,
            precio=item.producto.precio
        )
    
    productos_en_carrito.delete()
    return render(request, 'compra_exitosa.html', {'pedido': pedido})
