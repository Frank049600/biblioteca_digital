# Generated by Django 5.0.6 on 2024-08-12 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estadias', '0010_alter_model_estadias_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='model_estadias',
            name='matricula',
            field=models.CharField(default=4646225, max_length=255),
            preserve_default=False,
        ),
    ]
