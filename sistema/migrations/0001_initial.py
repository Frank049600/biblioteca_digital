# Generated by Django 5.0.4 on 2024-06-19 23:50

import django.db.models.manager
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UsuarioAcceso',
            fields=[
                ('cve_persona', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('login', models.CharField(max_length=10, unique=True, verbose_name='Nombre de usuario')),
                ('password', models.CharField(max_length=128)),
                ('activo', models.BooleanField(default=False)),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ('staff', models.BooleanField(default=False)),
                ('superuser', models.BooleanField(default=False)),
                ('last_login', models.DateTimeField(blank=True, editable=False, null=True)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('avatar', models.ImageField(blank=True, default='avatar/default.png', null=True, upload_to='avatar')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Acceso Usuario',
                'verbose_name_plural': 'Acceso Usuarios',
                # 'db_table': 'sistema_usuario',
            },
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]