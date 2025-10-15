from django.contrib import admin
from .models import Usuario, Ticket

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'correo', 'telefono', 'rol')
    search_fields = ('nombre', 'correo')

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('id', 'asunto', 'id_usuario', 'estado', 'creado_en')
    list_filter = ('estado',)
    search_fields = ('asunto', 'descripcion')
