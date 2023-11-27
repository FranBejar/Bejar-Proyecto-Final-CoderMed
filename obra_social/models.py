from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Hospital(models.Model):
    nombre=models.CharField(max_length=40)
    direccion=models.CharField(max_length=100)
    telefono=models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nombre}"

class Afiliado(models.Model):
    nombre=models.CharField(max_length=100)
    apellido=models.CharField(max_length=100)
    dni=models.CharField(max_length=10)
    telefono=models.CharField(max_length=20, blank=True)
    email=models.EmailField(max_length=32)
    fecha_de_nacimiento=models.DateField()
    direccion=models.CharField(max_length=50)
    plan=models.IntegerField()

    def __str__(self):
        return f"{self.dni} - {self.apellido}"

class Especialista(models.Model):
    nombre=models.CharField(max_length=100)
    apellido=models.CharField(max_length=100)
    especialidad=models.CharField(max_length=100)
    matricula=models.IntegerField()

    def __str__(self):
        return f"{self.especialidad} - {self.apellido}"

class Autorizacion(models.Model):
    creador = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    dni_afiliado=models.CharField(max_length=10)
    plan=models.IntegerField()
    hospital=models.CharField(max_length=40)
    especialista=models.CharField(max_length=200)
    intervencion=models.CharField(max_length=100)
    observaciones=models.TextField(blank=True)
    fecha_solicitud=models.DateTimeField(auto_now_add=True)
    solicitud_aprobada=models.BooleanField(default=False)

    def __str__(self):
        return f"{self.dni_afiliado} - {self.intervencion} - {self.fecha_solicitud}"
    
class Articulo(models.Model):
    titulo = models.CharField(max_length=50)
    subtitulo = models.CharField(max_length=100)
    cuerpo = models.TextField(blank=False)
    autor = models.CharField(max_length=50)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.titulo}"