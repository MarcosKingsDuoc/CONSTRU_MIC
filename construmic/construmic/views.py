from django.shortcuts import render

def index_page(request):
    return render(request, 'index.html')

def productos_page(request):
    return render(request, 'productos.html')

def ofertas_page(request):
    return render(request, 'ofertas.html')

def contacto_page(request):
    return render(request, 'contacto.html')

