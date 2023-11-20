# Generated by Django 4.2.6 on 2023-11-20 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Afiliado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('dni', models.CharField(max_length=10)),
                ('telefono', models.CharField(blank=True, max_length=20)),
                ('email', models.EmailField(max_length=32)),
                ('fecha_de_nacimiento', models.DateField()),
                ('direccion', models.CharField(max_length=50)),
                ('plan', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Autorizacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dni_afiliado', models.CharField(max_length=10)),
                ('plan', models.IntegerField()),
                ('hospital', models.CharField(max_length=40)),
                ('especialista', models.CharField(max_length=200)),
                ('intervencion', models.CharField(max_length=100)),
                ('observaciones', models.TextField(blank=True)),
                ('fecha_solicitud', models.DateTimeField(auto_now_add=True)),
                ('solicitud_aprobada', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Especialista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('especialidad', models.CharField(max_length=100)),
                ('matricula', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('direccion', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=20)),
            ],
        ),
    ]
