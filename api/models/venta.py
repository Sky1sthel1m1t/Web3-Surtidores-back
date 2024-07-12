from django.db import models


class Venta(models.Model):
    nombre_factura = models.CharField(max_length=100)
    nit = models.CharField(max_length=100)
    cliente = models.CharField(max_length=100)
    correo = models.CharField(max_length=100)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    precio_combustible = models.DecimalField(max_digits=10, decimal_places=2)
    litros = models.DecimalField(max_digits=10, decimal_places=2)
    combustible = models.ForeignKey(
        'Combustible',
        on_delete=models.CASCADE,
        related_name='venta_combustible'
    )
    bomba = models.ForeignKey(
        'Bomba',
        on_delete=models.CASCADE,
        related_name='venta_bomba'
    )
    fecha = models.DateTimeField(auto_now_add=True)
    hora = models.TimeField(auto_now_add=True)
    surtidor = models.ForeignKey(
        'Surtidor',
        on_delete=models.CASCADE,
        related_name='venta_surtidor'
    )
    is_anulada = models.BooleanField(default=False)