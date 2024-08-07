# Generated by Django 5.0.6 on 2024-07-12 09:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Combustible',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Surtidor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('latitud', models.CharField(max_length=100)),
                ('longitud', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Bomba',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=100)),
                ('combustibles', models.ManyToManyField(related_name='bombas_combustibles', to='api.combustible')),
                ('surtidor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bombas', to='api.surtidor')),
            ],
        ),
        migrations.CreateModel(
            name='TanqueGeneral',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capacidad', models.FloatField()),
                ('cantidad_actual', models.FloatField()),
                ('precio', models.FloatField()),
                ('combustible', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tanques_generales', to='api.combustible')),
                ('surtidor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tanques_generales', to='api.surtidor')),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_factura', models.CharField(max_length=100)),
                ('nit', models.CharField(max_length=100)),
                ('cliente', models.CharField(max_length=100)),
                ('correo', models.CharField(max_length=100)),
                ('monto', models.DecimalField(decimal_places=2, max_digits=10)),
                ('precio_combustible', models.DecimalField(decimal_places=2, max_digits=10)),
                ('litros', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('hora', models.TimeField(auto_now_add=True)),
                ('is_anulada', models.BooleanField(default=False)),
                ('bomba', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='venta_bomba', to='api.bomba')),
                ('combustible', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='venta_combustible', to='api.combustible')),
                ('surtidor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='venta_surtidor', to='api.surtidor')),
            ],
        ),
    ]
