from django.db import models
from django.core.validators import EmailValidator

class FormularioContacto(models.Model):
    nombre = models.CharField(max_length=64, default='')
    apellidos = models.CharField(max_length=64, default='')
    email = models.EmailField(max_length=64, default='', validators=[EmailValidator(message="Ingrese una dirección de correo electrónico válida.")])
    mensaje = models.CharField(max_length=2000, default='')

    def __str__(self):
        return f"{self.nombre} {self.apellidos}"

    class Meta:
        verbose_name = "Formulario de Contacto"
        verbose_name_plural = "Formularios de Contacto"
