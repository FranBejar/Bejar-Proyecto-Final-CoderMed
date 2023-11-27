# Generated by Django 4.2.6 on 2023-11-27 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('obra_social', '0002_autorizacion_creador'),
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('subtitulo', models.CharField(max_length=100)),
                ('cuerpo', models.TextField()),
                ('autor', models.CharField(max_length=50)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]