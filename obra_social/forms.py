from django import forms

from obra_social.models import Especialista,Hospital

class AfiliacionFormulario(forms.Form):
    nombre = forms.CharField(required=True, max_length=100)
    apellido = forms.CharField(required=True, max_length=100)
    dni = forms.CharField(required=True, max_length=10)
    telefono = forms.CharField(required=True, max_length=20)
    email = forms.CharField(required=True, max_length=32)
    fecha_de_nacimiento = forms.DateField(required=True, widget=forms.DateInput(attrs={'type': 'date'}))
    direccion = forms.CharField(required=True, max_length=50)
    plan_choices = [(100, 'Plan 100'), (200, 'Plan 200'), (300, 'Plan 300')]
    plan = forms.ChoiceField(choices=plan_choices, widget=forms.Select(), required=True)

class NuevoEspecialista(forms.Form):
    nombre = forms.CharField(required=True, max_length=100)
    apellido = forms.CharField(required=True, max_length=100)
    especialidad = forms.CharField(required=True, max_length=100)
    matricula = forms.IntegerField(required=True)

class NuevoHospital(forms.Form):
    nombre=forms.CharField(required=True, max_length=40)
    direccion=forms.CharField(required=True, max_length=100)
    telefono=forms.CharField(required=True, max_length=100)

class NuevaAutorizacion(forms.Form):
    dni_afiliado=forms.CharField(required=True, max_length=10)
    plan_choices = [(100, 'Plan 100'), (200, 'Plan 200'), (300, 'Plan 300')]
    plan = forms.ChoiceField(choices=plan_choices, widget=forms.Select())
    hospitales = Hospital.objects.all()
    hospital_choices = [(str(hospital), str(hospital)) for hospital in hospitales]
    hospital = forms.ChoiceField(choices=hospital_choices, widget=forms.Select())
    especialistas = Especialista.objects.all()
    especialista_choices = [(str(medico), str(medico)) for medico in especialistas]
    especialista = forms.ChoiceField(choices=especialista_choices, widget=forms.Select())
    intervencion = forms.CharField(required=True, max_length=100)
    observaciones = forms.CharField(required=False)