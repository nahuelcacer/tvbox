from django.db import models

# Create your models here.

class Servicio(models.Model):
    nombre = models.CharField(max_length=240)
    descripcion = models.CharField(max_length=240)

class Pack(models.Model):
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=240)
    descripcion = models.CharField(max_length=240)
    creado_en = models.DateTimeField(auto_now_add=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)  # Adjust max_digits and decimal_places as per your requirement
