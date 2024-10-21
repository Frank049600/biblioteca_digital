# Generated by Django 5.0.4 on 2024-05-16 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('almacen', '0006_alter_acervo_model_colocacion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acervo_model',
            name='estado',
            field=models.CharField(choices=[('EXC', 'Excelente'), ('BUE', 'Bueno'), ('REG', 'Regular'), ('MAL', 'Malo')], default='EXC', max_length=3, verbose_name='Estado del libro'),
        ),
    ]
