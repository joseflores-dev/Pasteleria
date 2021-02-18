from django.contrib import admin
from .models import Producto,Perfil,Reserva,Mensaje,Categoria
# Register your models here.

admin.site.register(Perfil)
admin.site.register(Reserva)
admin.site.register(Mensaje)
admin.site.register(Categoria)


