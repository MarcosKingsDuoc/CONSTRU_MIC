from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages

from .forms import SignInForm, SignUpForm
from .models import CustomUser

from django.contrib.auth import authenticate, login

def iniciar_sesion_page(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            correo = form.cleaned_data.get('correo')
            password = form.cleaned_data.get('password')
            print("Datos del formulario:", correo, password)  # Mensaje de depuración
            user = authenticate(request, correo=correo, password=password)
            if user is not None:
                login(request, user)
                return redirect('inicio_page')  # Redirecciona a la página de inicio después de iniciar sesión
            else:
                print("Error: El usuario no pudo ser autenticado")
        else:
            print("Error en la validación del formulario:", form.errors)
    else:
        form = SignInForm()
    return render(request, 'iniciar-sesion.html', {'form': form})


def registrarse_page(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            # Guardar el nuevo usuario en la base de datos
            user = form.save(commit=False)
            user.username = form.cleaned_data['correo']  # Usar el correo como nombre de usuario
            user.save()
            print("Usuario registrado correctamente:", form.cleaned_data)
            messages.success(request, '¡Usuario creado correctamente! Inicia sesión para continuar.')
            return redirect('registrarse_page')  # Redirigir al usuario a la página de inicio después del registro
        else:
            print("Formulario inválido:", form.errors)
    else:
        form = SignUpForm()
    return render(request, 'registrarse.html', {'form': form})

