from django.db import models
from servicios.models import Pack
from clientes.models import Cliente

class Suscripcion(models.Model):
    pack = models.ForeignKey(Pack, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    equipo = models.CharField(max_length=240, verbose_name="Equipo asociado")  # Nombre más descriptivo
    comienzo_suscripcion = models.DateTimeField()
    fin_suscripcion = models.DateTimeField()

    class Meta:
        unique_together = (('pack', 'cliente'),)  # Garantiza que un cliente solo pueda tener una suscripción al mismo pack

    def clean(self):
        if self.fin_suscripcion <= self.comienzo_suscripcion:
            raise ValidationError('La fecha de finalización de la suscripción debe ser posterior a la fecha de inicio.')

    def suscripcion_activa(self):
        return self.comienzo_suscripcion <= timezone.now() <= self.fin_suscripcion
