from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class SignUpForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['nombre', 'apellidos', 'correo', 'direccion', 'password']  # Excluir el campo 'username' del formulario


class SignInForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ('correo', 'password')
