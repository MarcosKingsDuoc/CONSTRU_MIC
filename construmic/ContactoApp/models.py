from django.db import models

class FormularioContacto(models.Model):
    nombres = models.CharField(max_length=64)
    correo = models.EmailField(max_length=64)
    mensaje = models.CharField(max_length=2000)
