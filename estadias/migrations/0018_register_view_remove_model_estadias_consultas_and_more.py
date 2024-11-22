# Generated by Django 5.0.4 on 2024-11-21 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estadias', '0017_rename_consulta_model_estadias_consultas'),
    ]

    operations = [
        migrations.CreateModel(
            name='register_view',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_reporte', models.IntegerField(null=True)),
                ('matricula', models.IntegerField(null=True)),
                ('consultas', models.IntegerField(null=True)),
                ('fecha_consulta', models.DateField(blank=True, null=True, verbose_name='Fecha de consulta')),
            ],
            options={
                'verbose_name': 'consulta',
                'verbose_name_plural': 'consultas',
            },
        ),
        migrations.RemoveField(
            model_name='model_estadias',
            name='consultas',
        ),
        migrations.RemoveField(
            model_name='model_estadias',
            name='fecha_consulta',
        ),
    ]