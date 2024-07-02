from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils import timezone
from django.contrib import messages
from .models import Producto, Carrito, CarritoProducto, Pedido, PedidoProducto 
from Accounts.models import CustomUser


def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'lista_productos.html', {'productos': productos})

def detalle_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    return render(request, 'detalle_producto.html', {'producto': producto})

@login_required
def agregar_al_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    
    if producto.stock == 0:
        messages.error(request, f'El producto {producto.nombre} está agotado.')
        return redirect('lista_productos')
    
    carrito, creado = Carrito.objects.get_or_create(usuario=request.user)
    carrito_producto, creado = CarritoProducto.objects.get_or_create(carrito=carrito, producto=producto)
    
    if not creado:
        if carrito_producto.cantidad < producto.stock:
            carrito_producto.cantidad += 1
            carrito_producto.save()
        else:
            messages.error(request, f'No hay suficiente stock para {producto.nombre}.')
    else:
        carrito_producto.cantidad = 1
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
        # Verificar que hay suficiente stock
        if item.producto.stock >= item.cantidad:
            PedidoProducto.objects.create(
                pedido=pedido,
                producto=item.producto,
                cantidad=item.cantidad,
                precio=item.producto.precio
            )
            # Restar la cantidad comprada del stock
            item.producto.stock -= item.cantidad
            item.producto.save()
        else:
            messages.error(request, f'No hay suficiente stock para {item.producto.nombre}.')
            return redirect('carrito')
    
    productos_en_carrito.delete()
    return render(request, 'compra_exitosa.html', {'pedido': pedido})


@login_required
def eliminar_del_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    carrito = get_object_or_404(Carrito, usuario=request.user)
    carrito_producto = get_object_or_404(CarritoProducto, carrito=carrito, producto=producto)
    carrito_producto.delete()
    return redirect('carrito')

@login_required
def cambiar_cantidad_producto(request, producto_id, operacion):
    producto = get_object_or_404(Producto, id=producto_id)
    carrito = get_object_or_404(Carrito, usuario=request.user)
    carrito_producto = get_object_or_404(CarritoProducto, carrito=carrito, producto=producto)
    
    if operacion == 'incrementar':
        if carrito_producto.cantidad < producto.stock:
            carrito_producto.cantidad += 1
            carrito_producto.save()
        else:
            messages.error(request, f'No hay suficiente stock para {producto.nombre}.')
    elif operacion == 'decrementar':
        if carrito_producto.cantidad > 1:
            carrito_producto.cantidad -= 1
            carrito_producto.save()
        else:
            carrito_producto.delete()
    
    return redirect('carrito')

# Vistas de administración
@user_passes_test(lambda u: u.is_staff)
@login_required
def admin_historial_compras(request):
    pedidos = Pedido.objects.all().order_by('-fecha')
    return render(request, 'admin/admin_historial_compras.html', {'pedidos': pedidos})

@user_passes_test(lambda u: u.is_staff)
@login_required
def admin_agregar_producto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        precio = request.POST.get('precio')
        stock = request.POST.get('stock')
        imagen = request.FILES.get('imagen')
        
        Producto.objects.create(nombre=nombre, descripcion=descripcion, precio=precio, stock=stock, imagen=imagen)
        return redirect('admin_lista_productos')
    
    return render(request, 'admin/admin_agregar_producto.html')

@user_passes_test(lambda u: u.is_staff)
@login_required
def admin_panel(request):    
    return render(request, 'admin/panel_administracion.html')


@user_passes_test(lambda u: u.is_staff) # editar productos como admin
@login_required
def admin_editar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        producto.nombre = request.POST.get('nombre')
        producto.descripcion = request.POST.get('descripcion')
        producto.precio = request.POST.get('precio')
        producto.stock = request.POST.get('stock')
        if request.FILES.get('imagen'):
            producto.imagen = request.FILES.get('imagen')
        producto.save()
        return redirect('admin_lista_productos')
    
    return render(request, 'admin/admin_editar_producto.html', {'producto': producto})

@user_passes_test(lambda u: u.is_staff) # eliminar productos admin
@login_required
def admin_eliminar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        producto.delete()
        return redirect('admin_lista_productos')
    
    return render(request, 'admin/admin_eliminar_producto.html', {'producto': producto})

@login_required
def admin_lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'admin/admin_lista_productos.html', {'productos': productos})




def error_403(request, exception=None):
    return render(request, 'error_403.html', status=403)


def buscar_productos(request):
    query = request.GET.get('q')
    productos = Producto.objects.filter(nombre__icontains=query) | Producto.objects.filter(descripcion__icontains=query)
    return render(request, 'resultados_busqueda.html', {'productos': productos, 'query': query})

@login_required
def admin_lista_usuarios(request):
    usuarios = CustomUser.objects.all()
    for usuario in usuarios:
        usuario.activar_desactivar_label = "Desactivar" if usuario.is_active else "Activar"
    return render(request, 'admin/admin_lista_usuarios.html', {'usuarios': usuarios})


@login_required
def admin_activar_desactivar_usuario(request, user_id):
    if request.user.id == user_id:
        messages.error(request, 'No puedes cambiar tu propio estado de actividad.')
        return redirect('admin_lista_usuarios')

    usuario = get_object_or_404(CustomUser, id=user_id)
    usuario.is_active = not usuario.is_active
    usuario.save()
    messages.success(request, f'El usuario {usuario.email} ha sido {"activado" if usuario.is_active else "desactivado"}.')
    return redirect('admin_lista_usuarios')

