from django.db import models

class Control(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=40)
    presupuesto = models.CharField(max_length=40)
    due_date = models.DateField()
    is_delivered = models.BooleanField()


    def __str__(self):
        is_delivered = 'Si' if self.is_delivered else 'No'
        return f'Nombre de la Entrega: {self.name} -- Fecha de entrega: {self.due_date} -- Presupuesto: {self.presupuesto} -- Entregado: {is_delivered} ' 

