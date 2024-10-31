# Generated by Django 5.0.4 on 2024-05-15 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='estadias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proyecto', models.CharField(max_length=150)),
                ('alumno', models.CharField(max_length=150)),
                ('asesor_academico', models.CharField(max_length=150)),
                ('generacion', models.CharField(max_length=12)),
                ('empresa', models.CharField(max_length=150)),
                ('asesor_empresarial', models.CharField(max_length=150)),
                ('carrera', models.CharField(blank=True, choices=[('ADC', 'ADC'), ('MET', 'MET'), ('QAI', 'QAI'), ('PIA', 'PIA'), ('QAM', 'QAM'), ('ERC', 'ERC'), ('IDGS', 'IDGS'), ('ITEA', 'ITEA'), ('IMET', 'IMET'), ('IER', 'IER'), ('ISIP', 'ISIP'), ('IPQ', 'IPQ'), ('LGCH', 'LGCH')], default='2', help_text='Prioridad de la tarea', max_length=20)),
                ('reporte', models.FileField(null=True, upload_to='documentos_pdf/')),
                ('convenio', models.FileField(null=True, upload_to='documentos_xlsx/')),
                ('c_aceptacion', models.FileField(null=True, upload_to='documentos_pdf/')),
                ('cronograma', models.FileField(null=True, upload_to='documentos_pdf/')),
            ],
            options={
                'verbose_name': 'estadias',
                'verbose_name_plural': 'estadias',
            },
        ),
    ]
