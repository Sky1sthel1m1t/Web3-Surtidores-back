from django.db import models


class Bomba(models.Model):
    surtidor = models.ForeignKey(
        'Surtidor',
        on_delete=models.CASCADE,
        related_name='bombas'
    )
    codigo = models.CharField(max_length=100)
    combustibles = models.ManyToManyField(
        'Combustible',
        related_name='bombas_combustibles',
        blank=False
    )