from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=64)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.CharField(max_length=32)
    alto = models.IntegerField()
    largo = models.IntegerField()
    ancho = models.IntegerField()
    peso = models.DecimalField(max_digits=6, decimal_places=2)
    descripcion = models.TextField()
    ESTADO_CHOICES = [
        (1, 'Nuevo'),
        (2, 'Usado'),
        (3, 'Reacondicionado'),
    ]
    estado = models.IntegerField(choices=ESTADO_CHOICES)
    imagen = models.BinaryField()

    def __str__(self):
        return f'{self.nombre} -> {self.precio}'

