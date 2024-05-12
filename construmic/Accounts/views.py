from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():

            form.save()
            messages.success(request, "¡Cuenta creada exitosamente! Por favor, inicie sesión.")
            return redirect('iniciar_sesion_page')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registrarse.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('inicio_page')  # Cambia 'home' por la URL a la que quieres redirigir después del inicio de sesión
    else:
        form = CustomAuthenticationForm()
    return render(request, 'iniciar-sesion.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('inicio_page')