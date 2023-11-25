from django.urls import path

from obra_social.views import (lista_planes,lista_medicos,lista_hospitales,nuevo_afiliado,bienvenido,
                               buscar_medico,formularios,form_completo,nuevo_especialista,nuevo_hospital,
                               nueva_solicitud,lista_autorizaciones,editar_autorizacion,preelimina_autorizacion,eliminar_autorizacion)

urlpatterns = [
    path("planes/",lista_planes, name="planes"),
    
    path("cartilla/",lista_medicos, name="cartilla"),
    path("especialista/",buscar_medico, name="especialista"),

    path("hospitales/",lista_hospitales, name="hospitales"),

    path("formularios/",formularios, name="formularios"),

    path("afiliate/",nuevo_afiliado, name="afiliate"),
    path("nuevo-especialista/",nuevo_especialista, name='nuevo-especialista'),
    path("nuevo-hospital/",nuevo_hospital, name='nuevo-hospital'),
    path("nueva-solicitud/",nueva_solicitud, name='nueva-solicitud'),

    path("bienvenido/",bienvenido, name="bienvenido"),
    path("form-completo/",form_completo, name="form-completo"),
    path("lista-autorizaciones/",lista_autorizaciones, name="lista-autorizaciones"),

    path("editar-autorizacion/<int:id>/",editar_autorizacion, name="editar-autorizacion"),
    path("cancelar-autorizacion/<int:id>/",preelimina_autorizacion, name="cancelar-autorizacion"),
    path("eliminar-autorizacion/<int:id>/",eliminar_autorizacion, name="eliminar-autorizacion"),
]