from django.shortcuts import render, redirect







def index_page(request):

    message = request.GET.get('message', None)
    return render(request, 'index.html', {'message': message})


def productos_page(request):

    return render(request, 'productos.html', )

def ofertas_page(request):
    return render(request, 'ofertas.html')





