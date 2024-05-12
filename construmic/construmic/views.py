from django.shortcuts import render, redirect
from django.contrib import messages




from CarritoApp.models import Producto

def index_page(request):

    message = request.GET.get('message', None)
    return render(request, 'index.html', {'message': message})


def productos_page(request):
    producutos = Producto.objects.all()
    return render(request, 'productos.html', {'productos':producutos})

def ofertas_page(request):
    return render(request, 'ofertas.html')





