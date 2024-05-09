from django.shortcuts import render, redirect
from django.contrib import messages
# Create your views here.

from ContactoApp.models import FormularioContacto 

def contacto_page(request):
    if request.method == 'POST':
        nombres = request.POST.get('nombres')
        correo = request.POST.get('correo')
        mensaje = request.POST.get('mensaje')
        if nombres and correo and mensaje:
            if len(mensaje) < 5:
                # Hacer algo si el mensaje es demasiado corto
                print("El mensaje es demasiado corto.")
                # Puedes mostrar una alerta o realizar alguna otra acción
                messages.warning(request, 'Su mensaje es muy corto. Por favor, escriba un mensaje de 5 o más carácteres.')

            else:
                contacto = FormularioContacto.objects.create(nombres=nombres, correo=correo, mensaje=mensaje)
                contacto.save()
                messages.success(request, '¡Mensaje enviado correctamente!')
                return redirect('contacto_page')
        else:
            messages.error(request, 'Por favor, complete todos los campos.')
    return render(request, 'contacto.html') 