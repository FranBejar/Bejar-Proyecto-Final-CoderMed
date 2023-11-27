from django.urls import path

from obra_social.views import (lista_planes,lista_medicos,lista_hospitales,nuevo_afiliado,bienvenido,
                               buscar_medico,formularios,form_completo,nuevo_especialista,nuevo_hospital,
                               nueva_solicitud,lista_autorizaciones,editar_autorizacion,preelimina_autorizacion,eliminar_autorizacion,
                               editar_especialista,preelimina_especialista,eliminar_especialista,editar_hospital,preelimina_hospital,
                               eliminar_hospital,about,pages,nuevo_articulo,editar_articulo,ver_articulo,
                               preelimina_articulo,eliminar_articulo)

urlpatterns = [
    path("planes/",lista_planes, name="planes"),
    path("about/",about,name='about'),

    path("pages/",pages,name='pages'),
    path("nuevo-articulo/",nuevo_articulo,name='nuevo-articulo'),
    path("ver-articulo/<int:id>/",ver_articulo,name='ver-articulo'),
    path("editar-articulo/<int:id>/",editar_articulo,name='editar-articulo'),
    path("eliminar-articulo/<int:id>/",preelimina_articulo,name='eliminar-articulo'),
    path("borrar-articulo/<int:id>/",eliminar_articulo,name='borrar-articulo'),
    
    path("cartilla/",lista_medicos, name="cartilla"),
    path("especialista/",buscar_medico, name="especialista"),

    path("hospitales/",lista_hospitales, name="hospitales"),

    path("formularios/",formularios, name="formularios"),

    path("afiliate/",nuevo_afiliado, name="afiliate"),

    path("nuevo-especialista/",nuevo_especialista, name='nuevo-especialista'),
    path("editar-especialista/<int:id>/",editar_especialista,name='editar-especialista'),
    path("eliminar-especialista/<int:id>/",preelimina_especialista,name='eliminar-especialista'),
    path("borrar-especialista/<int:id>/",eliminar_especialista,name='borrar-especialista'),

    path("nuevo-hospital/",nuevo_hospital, name='nuevo-hospital'),
    path("editar-hospital/<int:id>/",editar_hospital, name='editar-hospital'),
    path("eliminar-hospital/<int:id>/",preelimina_hospital,name='eliminar-hospital'),
    path("borrar-hospital/<int:id>/",eliminar_hospital,name='borrar-hospital'),

    path("nueva-solicitud/",nueva_solicitud, name='nueva-solicitud'),

    path("bienvenido/",bienvenido, name="bienvenido"),
    path("form-completo/",form_completo, name="form-completo"),
    path("lista-autorizaciones/",lista_autorizaciones, name="lista-autorizaciones"),

    path("editar-autorizacion/<int:id>/",editar_autorizacion, name="editar-autorizacion"),
    path("cancelar-autorizacion/<int:id>/",preelimina_autorizacion, name="cancelar-autorizacion"),
    path("eliminar-autorizacion/<int:id>/",eliminar_autorizacion, name="eliminar-autorizacion"),
]