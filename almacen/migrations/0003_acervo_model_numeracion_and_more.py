# Generated by Django 5.0.4 on 2024-05-16 05:03

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('almacen', '0002_acervo_model_estado_acervo_model_type_adqui_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='acervo_model',
            name='numeracion',
            field=models.IntegerField(default='001', verbose_name='Numeración para colocación'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='acervo_model',
            name='colocacion',
            field=models.CharField(choices=[('ADM', 'Administración'), ('PIA', 'Procesos_Industriales'), ('MET', 'Mecatrónica'), ('ERC', 'Energías_Renovables'), ('QUIM', 'Química'), ('TIS', 'Tecnologías_Información'), ('CBA', 'Ciencias_Básicas_Aplicadas'), ('FSC', 'Formación_Sociocultural'), ('OCL', 'Otros_Conocimientos'), ('OCLEC', 'Lectura'), ('OCA', 'Adicciones'), ('OCIG', 'Igualdad'), ('FCE', 'Colecciones_Ciencia'), ('IDI', 'Idiomas'), ('IDF', 'Francés'), ('LYMd', 'CA_LYM'), ('ADMd', 'CA_ADM'), ('QUIMd', 'CA_QUIM'), ('METd', 'CA_MET'), ('PIAd', 'CA_PIA'), ('ERCd', 'CA_ERC'), ('CBAd', 'CA_CBA'), ('FSCd', 'CA_FSC'), ('OCId', 'CA_OCI'), ('TISd', 'CA_TIS'), ('OC', 'Hemerografico'), ('OTROS', 'Otros')], default='ADM', max_length=6, verbose_name='Colocación'),
        ),
    ]
