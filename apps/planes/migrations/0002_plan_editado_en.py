# Generated by Django 5.0.3 on 2024-03-18 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='editado_en',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
