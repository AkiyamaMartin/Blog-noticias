from django.contrib import admin
from .models import Evento

# Register your models here.


class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria','colectividad', 'hora', 'lugar','creado', 'modificado',)
    list_filter = ('creado', 'categoria', 'colectividad')
    search_fields = ('titulo', 'descripcion')
    prepopulated_fields = {'slug': ('titulo',)} 
    date_hierarchy = 'fecha' 

# Registra tu modelo con esta personalización:
admin.site.register(Evento, EventoAdmin)