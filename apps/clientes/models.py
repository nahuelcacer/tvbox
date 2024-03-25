from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=240)
    dni = models.CharField(max_length=12)
    

class Contacto(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    celular = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)  # Cambiado a EmailField para validar formato de correo electrónico

class Direccion(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    nombre_calle = models.CharField(max_length=100)
    numero_calle = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=100, blank=True)  # Ejemplo de campo adicional
    estado = models.CharField(max_length=100, blank=True)  # Ejemplo de campo adicional
    pais = models.CharField(max_length=100, blank=True)  # Ejemplo de campo adicional
    codigo_postal = models.CharField(max_length=20, blank=True)  # Ejemplo de campo adicional
    latitud = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    longitud = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)

    class Meta:
        indexes = [
            models.Index(fields=['latitud', 'longitud']),
            models.Index(fields=['cliente']),  # Ejemplo de índice adicional
        ]

    # Ejemplo de método para obtener la dirección completa
    def direccion_completa(self):
        return f"{self.nombre_calle} {self.numero_calle}"
