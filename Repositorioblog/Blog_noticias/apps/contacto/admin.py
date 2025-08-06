from django.contrib import admin
from .models import Contacto


class ContactoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'direccion', 'telefono', 'email_1', 'email_2', 'facebook','instagram','twitter', 'contenido')

    search_fields = ('titulo',)
    


admin.site.register(Contacto, ContactoAdmin)


    
