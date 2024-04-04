from django.shortcuts import render

def index_page(request):
    return render(request, 'index.html')

def productos_page(request):
    return render(request, 'productos.html')