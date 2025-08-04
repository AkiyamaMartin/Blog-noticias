from django.contrib import admin
from .models import Categoria, TipoCategoria
# Register your models here.


# Registra tu modelo con esta personalización:
admin.site.register(Categoria)
admin.site.register(TipoCategoria)