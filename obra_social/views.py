from django.shortcuts import render, redirect
from django.urls import reverse

from obra_social.forms import AfiliacionFormulario,NuevoEspecialista,NuevoHospital,NuevaAutorizacion
from obra_social.models import Afiliado,Especialista,Hospital,Autorizacion

# Create your views here.

def lista_planes(request):
    contexto={}
    http_response = render(
        request=request,
        template_name='obra_social/planes.html',
        context=contexto
    )
    return http_response

def lista_medicos(request):
    contexto = {
        "medicos": Especialista.objects.all()
    }
    http_response = render(
        request=request,
        template_name='obra_social/cartilla.html',
        context=contexto
    )
    return http_response

def buscar_medico(request):
    busqueda = request.POST.get("busqueda", "")
    
    if busqueda:
        medicos = Especialista.objects.filter(especialidad__contains=busqueda)
    else:
        medicos = Especialista.objects.all()

    contexto = {
        "medicos": medicos,
        "busqueda_form": busqueda,
    }

    return render(
        request=request,
        template_name='obra_social/cartilla.html',
        context=contexto
    )

def lista_hospitales(request):
    contexto = {
        "hospitales": Hospital.objects.all()
    }
    http_response = render(
        request=request,
        template_name='obra_social/hospitales.html',
        context=contexto
    )
    return http_response

def formularios(request):
    contexto={}
    http_response = render(
        request=request,
        template_name='obra_social/formularios.html',
        context=contexto
    )
    return http_response

def nuevo_afiliado(request):
    if request.method == "POST":
        formulario = AfiliacionFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            afiliado = Afiliado(
                nombre=data['nombre'],
                apellido=data['apellido'],
                dni=data['dni'],
                telefono=data['telefono'],
                email=data['email'],
                fecha_de_nacimiento=data['fecha_de_nacimiento'],
                direccion=data['direccion'],
                plan=data['plan']
            )
            afiliado.save()
            url_exitosa = reverse('bienvenido')
            return redirect(url_exitosa)
    else:
        formulario = AfiliacionFormulario()

    http_response = render(
        request=request,
        template_name='obra_social/afiliarse.html',
        context={'formulario': formulario}
    )
    return http_response

def nuevo_especialista(request):
    if request.method == "POST":
        formulario = NuevoEspecialista(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            especialista = Especialista(
                nombre=data['nombre'],
                apellido=data['apellido'],
                especialidad=data['especialidad'],
                matricula=data['matricula']
            )
            especialista.save()
            url_exitosa = reverse('form-completo')
            return redirect(url_exitosa)
    else:
        formulario = NuevoEspecialista()

    http_response = render(
        request=request,
        template_name='obra_social/nuevo-especialista.html',
        context={'formulario': formulario}
    )
    return http_response

def nuevo_hospital(request):
    if request.method == "POST":
        formulario = NuevoHospital(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            hospital = Hospital(
                nombre=data['nombre'],
                direccion=data['direccion'],
                telefono=data['telefono']
            )
            hospital.save()
            url_exitosa = reverse('form-completo')
            return redirect(url_exitosa)
    else:
        formulario = NuevoHospital()

    http_response = render(
        request=request,
        template_name='obra_social/nuevo-hospital.html',
        context={'formulario': formulario}
    )
    return http_response

def nueva_solicitud(request):
    if request.method == "POST":
        formulario = NuevaAutorizacion(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            autorizacion = Autorizacion(
                dni_afiliado=data['dni_afiliado'],
                plan=data['plan'],
                hospital=data['hospital'],
                especialista=data['especialista'],
                intervencion=data['intervencion'],
                observaciones=data['observaciones']
            )
            autorizacion.save()
            url_exitosa = reverse('form-completo')
            return redirect(url_exitosa)
    else:
        formulario = NuevaAutorizacion()

    http_response = render(
        request=request,
        template_name='obra_social/autorizar.html',
        context={'formulario': formulario}
    )
    return http_response

def bienvenido(request):
    contexto={}
    http_response = render(
        request=request,
        template_name='obra_social/bienvenido.html',
        context=contexto
    )
    return http_response

def form_completo(request):
    contexto={}
    http_response = render(
        request=request,
        template_name='obra_social/form-completo.html',
        context=contexto
    )
    return http_response