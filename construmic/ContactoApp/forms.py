from django import forms
from .models import FormularioContacto

class FormularioContactoForm(forms.ModelForm):
    class Meta:
        model = FormularioContacto
        fields = ['nombre', 'apellidos', 'email', 'mensaje']
