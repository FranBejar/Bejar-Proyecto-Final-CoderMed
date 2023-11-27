from django.contrib import admin
from django.urls import path

from perfiles.views import registro,login_view,CustomLogoutView,usuarios,MiPerfilUpdateView

urlpatterns = [
    path("usuarios/",usuarios,name="usuarios"),
    path("registro/",registro,name="registro"),
    path("login/",login_view,name="login"),
    path('logout/',CustomLogoutView.as_view(),name="logout"),
    path('editar-perfil/',MiPerfilUpdateView.as_view(),name="editar-perfil")
]