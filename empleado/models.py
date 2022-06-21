from django.db import models

class Empleado(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    grupo = models.CharField(max_length=40)
    planta = models.CharField(max_length=40)
    telefono = models.IntegerField()

    def __str__(self):
        return f'Nombre del Empleado: {self.nombre} {self.apellido} -- '