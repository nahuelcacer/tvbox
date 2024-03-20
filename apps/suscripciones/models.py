from django.db import models
from apps.planes.models import Plan
from apps.clientes.models import Cliente
from django.utils import timezone
class Suscripcion(models.Model):
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE, default=None)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    equipo = models.CharField(max_length=240, verbose_name="Equipo asociado")  # Nombre más descriptivo
    comienzo_suscripcion = models.DateTimeField()
    fin_suscripcion = models.DateTimeField()
    estado = models.BooleanField()

    class Meta:
        unique_together = (('plan', 'cliente'),)  # Garantiza que un cliente solo pueda tener una suscripción al mismo pack

    def clean(self):
        if self.fin_suscripcion <= self.comienzo_suscripcion:
            raise ValidationError('La fecha de finalización de la suscripción debe ser posterior a la fecha de inicio.')

    def suscripcion_activa(self):
        return self.comienzo_suscripcion <= timezone.now() <= self.fin_suscripcion

    def comienzo_suscripcion_str(self):
        return self.comienzo_suscripcion.strftime("%d-%m-%Y")
    def fin_suscripcion_str(self):
        return self.fin_suscripcion.strftime("%d-%m-%Y")
    
    def dias_vencidos(self):
        dias_restantes = (self.fin_suscripcion - timezone.now()).days
        return f"{dias_restantes} días"
   