from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from obra_social.forms import AfiliacionFormulario,NuevoEspecialista,NuevoHospital,NuevaAutorizacion,NuevoArticulo
from obra_social.models import Afiliado,Especialista,Hospital,Autorizacion,Articulo

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

@login_required
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

@login_required
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

@login_required
def editar_especialista(request,id):
    especialista = Especialista.objects.get(id=id)
    if request.method == "POST":
        formulario = NuevoEspecialista(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            especialista.nombre=data['nombre']
            especialista.apellido=data['apellido']
            especialista.especialidad=data['especialidad']
            especialista.matricula=data['matricula']
            especialista.save()
            url_exitosa = reverse('form-completo')
            return redirect(url_exitosa)
    else:
        inicial = {
            'nombre': especialista.nombre,
            'apellido': especialista.apellido,
            'especialidad': especialista.especialidad,
            'matricula': especialista.matricula
        }
        formulario = NuevoEspecialista(initial=inicial)
    http_response = render(
        request=request,
        template_name='obra_social/nuevo-especialista.html',
        context={'formulario': formulario}
    )
    return http_response

@login_required
def preelimina_especialista(request,id):
    contexto = {
        "especialista": Especialista.objects.get(id=id)
    }
    http_response = render(
        request=request,
        template_name='obra_social/eliminar-especialista.html',
        context=contexto
    )
    return http_response

@login_required
def eliminar_especialista(request,id):
    especialista = Especialista.objects.get(id=id)
    if request.method == "POST":
        especialista.delete()
        url_exitosa = reverse('cartilla')
        return redirect(url_exitosa)

@login_required
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

@login_required
def editar_hospital(request,id):
    hospital = Hospital.objects.get(id=id)
    if request.method == "POST":
        formulario = NuevoHospital(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            hospital.nombre = data['nombre']
            hospital.direccion = data['direccion']
            hospital.telefono = data['telefono']
            hospital.save()
            url_exitosa = reverse('form-completo')
            return redirect(url_exitosa)
    else:
        inicial = {
            'nombre': hospital.nombre,
            'direccion': hospital.direccion,
            'telefono': hospital.telefono
        }
        formulario = NuevoHospital(initial=inicial)

    http_response = render(
        request=request,
        template_name='obra_social/nuevo-hospital.html',
        context={'formulario': formulario}
    )
    return http_response

@login_required
def preelimina_hospital(request,id):
    contexto = {
        "hospital": Hospital.objects.get(id=id)
    }
    http_response = render(
        request=request,
        template_name='obra_social/eliminar-hospital.html',
        context=contexto
    )
    return http_response

@login_required
def eliminar_hospital(request,id):
    hospital = Hospital.objects.get(id=id)
    if request.method == "POST":
        hospital.delete()
        url_exitosa = reverse('hospitales')
        return redirect(url_exitosa)

@login_required
def nueva_solicitud(request):
    if request.method == "POST":
        formulario = NuevaAutorizacion(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            autorizacion = Autorizacion(
                creador=request.user,
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

def about(request):
    contexto={}
    http_response = render(
        request=request,
        template_name='obra_social/about-us.html',
        context=contexto
    )
    return http_response

@login_required
def form_completo(request):
    contexto={}
    http_response = render(
        request=request,
        template_name='obra_social/form-completo.html',
        context=contexto
    )
    return http_response

@login_required
def lista_autorizaciones(request):
    contexto = {
        "autorizaciones": Autorizacion.objects.all()
    }
    http_response = render(
        request=request,
        template_name='obra_social/autorizaciones.html',
        context=contexto
    )
    return http_response

@login_required
def preelimina_autorizacion(request,id):
    contexto = {
        "autorizacion": Autorizacion.objects.get(id=id)
    }
    http_response = render(
        request=request,
        template_name='obra_social/cancelar-autorizacion.html',
        context=contexto
    )
    return http_response

@login_required
def eliminar_autorizacion(request,id):
    autorizacion = Autorizacion.objects.get(id=id)
    if request.method == "POST":
        autorizacion.delete()
        url_exitosa = reverse('lista-autorizaciones')
        return redirect(url_exitosa)
    
@login_required
def editar_autorizacion(request,id):
    autorizacion = Autorizacion.objects.get(id=id)
    if request.method == "POST":
        formulario = NuevaAutorizacion(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            autorizacion.dni_afiliado=data['dni_afiliado']
            autorizacion.plan = int(data['plan'])
            autorizacion.hospital=data['hospital']
            autorizacion.especialista=data['especialista']
            autorizacion.intervencion=data['intervencion']
            autorizacion.observaciones=data['observaciones']
            autorizacion.save()
            url_exitosa = reverse('form-completo')
            return redirect(url_exitosa)
    else:
        inicial = {
            'dni_afiliado': autorizacion.dni_afiliado,
            'plan':str(autorizacion.plan),
            'hospital': str(autorizacion.hospital),
            'especialista': str(autorizacion.especialista),
            'intervencion': autorizacion.intervencion,
            'observaciones': autorizacion.observaciones
        }
        formulario = NuevaAutorizacion(initial=inicial)
    http_response = render(
        request=request,
        template_name='obra_social/autorizar.html',
        context={'formulario': formulario}
    )
    return http_response

def pages(request):
    articulos = Articulo.objects.all()
    if len(articulos) > 0:
        contexto = {"articulos": articulos}
    else:
        contexto = {"mensaje": "Aún no se compartieron noticias."}

    http_response = render(
        request=request,
        template_name='obra_social/noticias.html',
        context=contexto
    )
    return http_response

@login_required
def nuevo_articulo(request):
    if request.method == "POST":
        formulario = NuevoArticulo(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            articulo = Articulo(
                titulo = data['titulo'],
                subtitulo = data['subtitulo'],
                cuerpo = data['cuerpo'],
                autor = data['autor']
            )
            articulo.save()
            url_exitosa = reverse('pages')
            return redirect(url_exitosa)
    else:
        formulario = NuevoArticulo()

    http_response = render(
        request=request,
        template_name='obra_social/nueva-noticia.html',
        context={'formulario': formulario}
    )
    return http_response

def ver_articulo(request,id):
    contexto = {
        "articulo": Articulo.objects.get(id=id)
    }
    http_response = render(
        request=request,
        template_name='obra_social/articulo.html',
        context=contexto
    )
    return http_response

@login_required
def editar_articulo(request,id):
    articulo = Articulo.objects.get(id=id)
    if request.method == "POST":
        formulario = NuevoArticulo(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            articulo.titulo = data['titulo']
            articulo.subtitulo = data['subtitulo']
            articulo.cuerpo = data['cuerpo']
            articulo.autor = data['autor']
            articulo.save()
            url_exitosa = reverse('pages')
            return redirect(url_exitosa)
    else:
        inicial = {
            'titulo': articulo.titulo,
            'subtitulo': articulo.subtitulo,
            'cuerpo': articulo.cuerpo,
            'autor': articulo.autor
        }
        formulario = NuevoArticulo(initial=inicial)
    http_response = render(
        request=request,
        template_name='obra_social/nueva-noticia.html',
        context={'formulario': formulario}
    )
    return http_response

@login_required
def preelimina_articulo(request,id):
    contexto = {
        "articulo": Articulo.objects.get(id=id)
    }
    http_response = render(
        request=request,
        template_name='obra_social/eliminar-articulo.html',
        context=contexto
    )
    return http_response

@login_required
def eliminar_articulo(request,id):
    articulo = Articulo.objects.get(id=id)
    if request.method == "POST":
        articulo.delete()
        url_exitosa = reverse('pages')
        return redirect(url_exitosa)