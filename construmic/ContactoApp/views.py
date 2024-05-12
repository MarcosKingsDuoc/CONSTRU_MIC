from django.shortcuts import render, redirect
from django.contrib import messages
# Create your views here.

from ContactoApp.forms import FormularioContactoForm 

# def contacto_page(request):
#     if request.method == 'POST':
#         nombre = request.POST.get('nombre')
#         apellidos = request.POST.get('apellidos')
#         email = request.POST.get('email')
#         mensaje = request.POST.get('mensaje')
#         if nombre and apellidos and email and mensaje:
#             if len(mensaje) < 5:
#                 # Hacer algo si el mensaje es demasiado corto
#                 print("El mensaje es demasiado corto.")
#                 # Puedes mostrar una alerta o realizar alguna otra acción
#                 messages.warning(request, 'Su mensaje es muy corto. Por favor, escriba un mensaje de 5 o más carácteres.')

#             else:
#                 contacto = FormularioContacto.objects.create(nombre=nombre, apellidos=apellidos, correo=email, mensaje=mensaje)
#                 contacto.save()
#                 messages.success(request, '¡Mensaje enviado correctamente!')
#                 return redirect('contacto_page')
#         else:
#             messages.error(request, 'Por favor, complete todos los campos.')
#     return render(request, 'contacto.html') 

def contacto_page(request):
    if request.method == 'POST':
        form = FormularioContactoForm(request.POST)
        mensaje = request.POST.get('mensaje')
        if form.is_valid():
            if len(mensaje) < 5:
                messages.error(request, 'Su mensaje es muy corto. Por favor, escriba un mensaje de 5 o más carácteres.')
            else:
                form.save()
                messages.success(request, "¡Mensaje enviado exitosamente!")
                return redirect('contacto_page')
    else:
        form = FormularioContactoForm()  # Crear una instancia del formulario vacío para mostrar en GET request
    return render(request, 'contacto.html', {'form': form})  # Pasar el formulario como contexto al template
