# Generated by Django 5.0.4 on 2024-12-05 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0010_alter_model_catalogo_fechae_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='model_catalogo',
            name='entrega',
            field=models.CharField(blank=True, choices=[('No/entregado', 'No/entregado'), ('Entregado', 'Entregado'), ('Devuelto', 'Devuelto')], default='No/entregado', max_length=255, null=True, verbose_name='Tipo de entrega'),
        ),
    ]
