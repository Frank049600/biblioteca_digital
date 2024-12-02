# Generated by Django 5.0.4 on 2024-12-02 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0007_alter_model_catalogo_entrega'),
    ]

    operations = [
        migrations.AddField(
            model_name='model_catalogo',
            name='fechaE',
            field=models.DateTimeField(null=True, verbose_name='Fecha entrega'),
        ),
        migrations.AlterField(
            model_name='model_catalogo',
            name='fechaP',
            field=models.DateTimeField(null=True, verbose_name='Fecha prestamo'),
        ),
    ]