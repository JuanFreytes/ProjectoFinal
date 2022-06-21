from django.db import models


class Reclamo(models.Model):
    nombre = models.CharField(max_length=40)
    telefono = models.IntegerField()
    fecha = models.CharField(max_length=40)
    planta = models.CharField(max_length=40)

    descripcion = models.TextField(blank = True, null=True)


    def __str__(self):
        return f'{self.nombre} {self.planta}'