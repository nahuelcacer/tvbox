# Generated by Django 5.0.3 on 2024-03-19 13:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clientes', '0001_initial'),
        ('planes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Suscripcion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equipo', models.CharField(max_length=240, verbose_name='Equipo asociado')),
                ('comienzo_suscripcion', models.DateTimeField()),
                ('fin_suscripcion', models.DateTimeField()),
                ('estado', models.BooleanField()),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes.cliente')),
                ('plan', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='planes.plan')),
            ],
            options={
                'unique_together': {('plan', 'cliente')},
            },
        ),
    ]
