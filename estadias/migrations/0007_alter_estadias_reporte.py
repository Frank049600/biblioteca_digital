# Generated by Django 5.0.6 on 2024-07-09 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estadias', '0006_remove_estadias_c_aceptacion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estadias',
            name='reporte',
            field=models.FileField(blank=True, null=True, upload_to='reporte/', verbose_name='Reporte'),
        ),
    ]
