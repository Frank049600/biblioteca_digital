# Generated by Django 5.0.4 on 2024-05-18 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estadias', '0003_alter_estadias_c_aceptacion_alter_estadias_convenio_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estadias',
            name='c_aceptacion',
            field=models.FileField(null=True, upload_to='estadias'),
        ),
        migrations.AlterField(
            model_name='estadias',
            name='convenio',
            field=models.FileField(null=True, upload_to='estadias'),
        ),
        migrations.AlterField(
            model_name='estadias',
            name='cronograma',
            field=models.FileField(null=True, upload_to='estadias'),
        ),
        migrations.AlterField(
            model_name='estadias',
            name='reporte',
            field=models.FileField(null=True, upload_to='estadias'),
        ),
    ]
