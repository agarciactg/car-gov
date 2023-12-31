# Generated by Django 3.1 on 2021-09-03 12:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmailTemplate',
            fields=[
                ('id', models.CharField(choices=[('WELCOME_EMAIL', 'Plantilla de correo de bienvenida.'), ('VALIDATION_EMAIL', 'Plantilla de correo de confirmacion de email'), ('CONTRACT_AUTOPAY', 'Plantilla de correo de contrato de rental.'), ('RECOVERY_PASSWORD', 'Plantilla de correo de recuperacion de contraseña')], max_length=50, primary_key=True, serialize=False)),
                ('sengrid_id', models.CharField(help_text='Sengrid ID', max_length=340, verbose_name='Sengrid ID')),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Plantilla Email',
                'verbose_name_plural': 'Plantillas Email',
            },
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.PositiveSmallIntegerField(choices=[(1, 'Activo'), (2, 'Inactivo')], default=1, verbose_name='Estado')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha Creación')),
                ('date_updated', models.DateTimeField(auto_now=True, null=True, verbose_name='Fecha Actualizado')),
                ('name', models.CharField(max_length=340, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'Provincia',
                'verbose_name_plural': 'Provincias',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='TypeDocument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.PositiveSmallIntegerField(choices=[(1, 'Activo'), (2, 'Inactivo')], default=1, verbose_name='Estado')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha Creación')),
                ('date_updated', models.DateTimeField(auto_now=True, null=True, verbose_name='Fecha Actualizado')),
                ('name', models.CharField(max_length=340, verbose_name='Nombre')),
                ('initials', models.CharField(blank=True, max_length=340, null=True, verbose_name='Iniciales')),
                ('type_user', models.PositiveSmallIntegerField(choices=[(1, 'Natural'), (2, 'Empresa')], verbose_name='Tipo de Usuario')),
            ],
            options={
                'verbose_name': 'Tipo de Documento',
                'verbose_name_plural': 'Tipo de Documentos',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.PositiveSmallIntegerField(choices=[(1, 'Activo'), (2, 'Inactivo')], default=1, verbose_name='Estado')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha Creación')),
                ('date_updated', models.DateTimeField(auto_now=True, null=True, verbose_name='Fecha Actualizado')),
                ('name', models.CharField(max_length=340, verbose_name='Nombre')),
                ('province', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cities', to='base.province', verbose_name='Provincia')),
            ],
            options={
                'verbose_name': 'Ciudad',
                'verbose_name_plural': 'Ciudades',
                'ordering': ['id'],
            },
        ),
    ]
