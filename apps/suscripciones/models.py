from django.db import models
from apps.planes.models import Plan
from apps.clientes.models import Cliente

class Suscripcion(models.Model):
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE, default=None)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    equipo = models.CharField(max_length=240, verbose_name="Equipo asociado")  # Nombre más descriptivo
    comienzo_suscripcion = models.DateTimeField()
    fin_suscripcion = models.DateTimeField()

    class Meta:
        unique_together = (('plan', 'cliente'),)  # Garantiza que un cliente solo pueda tener una suscripción al mismo pack

    def clean(self):
        if self.fin_suscripcion <= self.comienzo_suscripcion:
            raise ValidationError('La fecha de finalización de la suscripción debe ser posterior a la fecha de inicio.')

    def suscripcion_activa(self):
        return self.comienzo_suscripcion <= timezone.now() <= self.fin_suscripcion
