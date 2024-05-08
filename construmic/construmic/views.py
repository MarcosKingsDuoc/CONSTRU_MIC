from django.shortcuts import render

from CarritoApp.models import Producto

def index_page(request):
    return render(request, 'index.html')

def productos_page(request):
    producutos = Producto.objects.all()
    return render(request, 'productos.html', {'productos':producutos})

def ofertas_page(request):
    return render(request, 'ofertas.html')

def contacto_page(request):
    return render(request, 'contacto.html')

