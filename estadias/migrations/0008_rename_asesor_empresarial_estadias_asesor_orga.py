# Generated by Django 5.0.6 on 2024-08-03 00:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estadias', '0007_alter_estadias_reporte'),
    ]

    operations = [
        migrations.RenameField(
            model_name='estadias',
            old_name='asesor_empresarial',
            new_name='asesor_orga',
        ),
    ]
