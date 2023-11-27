from django.contrib import admin

# Register your models here.
from obra_social.models import Hospital, Afiliado, Especialista, Autorizacion, Articulo

admin.site.register(Hospital)
admin.site.register(Afiliado)
admin.site.register(Especialista)
admin.site.register(Autorizacion)
admin.site.register(Articulo)