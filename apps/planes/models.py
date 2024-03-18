from django.db import models
from apps.servicios.models import Servicio
# Create your models here.
class Plan(models.Model):
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=240)
    descripcion = models.CharField(max_length=240)
    creado_en = models.DateTimeField(auto_now_add=True)
    editado_en = models.DateTimeField(auto_now=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)  # Adjust max_digits and decimal_places as per your requirement



    def fecha_editado_str(self):
        return self.editado_en.strftime("%d-%m-%Y")
    
    def fecha_creacion_str(self):
        return self.creado_en.strftime("%d-%m-%Y")

    def precio_str(self):
        return "$ " + str(self.precio)