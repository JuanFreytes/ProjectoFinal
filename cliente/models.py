from django.db import models


class Cliente(models.Model):
    name = models.CharField(max_length=40)
    address = models.CharField(max_length=40)
    email = models.EmailField()
    telefono = models.CharField(max_length=40)
    

    def __str__(self):
        return f'Nombre del Cliente: {self.name} -- Teléfono {self.telefono}--'
