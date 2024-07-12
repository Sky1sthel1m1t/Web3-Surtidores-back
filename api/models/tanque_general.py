from django.db import models


class TanqueGeneral(models.Model):
    capacidad = models.FloatField()
    cantidad_actual = models.FloatField()
    precio = models.FloatField()
    combustible = models.ForeignKey(
        'Combustible',
        on_delete=models.CASCADE,
        related_name='tanques_generales'
    )
    surtidor = models.ForeignKey(
        'Surtidor',
        on_delete=models.CASCADE,
        related_name='tanques_generales'
    )