from django.contrib import admin
from .models import Nosotros


class NosotrosAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'slug', 'creado', 'modificado', )
    prepopulated_fields = {'slug': ('titulo',)} 
    search_fields = ('titulo', 'contenido')
    date_hierarchy = 'creado' 


admin.site.register(Nosotros, NosotrosAdmin)