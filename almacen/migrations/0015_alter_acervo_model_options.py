# Generated by Django 5.0.6 on 2024-08-06 03:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('almacen', '0014_rename_fecharegistro_acervo_model_fecha_registro_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='acervo_model',
            options={'verbose_name': 'Acervo registros'},
        ),
    ]
