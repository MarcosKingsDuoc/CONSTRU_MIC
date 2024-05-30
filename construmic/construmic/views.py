from django.shortcuts import render, redirect


def index_page(request):
    message = request.GET.get('message', None)
    return render(request, 'index.html', {'message': message})


def sobre_nosotros_page(request):
    return render(request, 'sobre_nosotros.html')



