from django.contrib import admin
from .models import Articulo
# Register your models here.

#admin.site.register(articulo)

# Personalización del modelo en el admin: 
class ArticuloAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'creado', 'modificado', 'comentarios_habilitados', 'visitas', 'likes')
    list_filter = ('creado', 'modificado', 'comentarios_habilitados')
    search_fields = ('titulo', 'contenido', 'descripcion')
    prepopulated_fields = {'slug': ('titulo',)} 
    date_hierarchy = 'creado' 

# Registra tu modelo con esta personalización:
admin.site.register(Articulo, ArticuloAdmin)