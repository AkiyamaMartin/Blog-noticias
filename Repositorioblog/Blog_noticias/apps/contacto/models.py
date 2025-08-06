from django.db import models
from django.urls import reverse_lazy
from ckeditor.fields import RichTextField

class Contacto(models.Model):

    titulo = models.CharField(max_length=100, default='Contacto...') #nomrbe de la colect

    direccion = models.TextField(max_length=200)

    telefono = models.CharField(max_length=25)

    email_1 = models.EmailField()

    email_2 = models.EmailField(blank=True, null=True)

    #redes

    facebook = models.URLField(blank=True,null=True)

    instagram = models.URLField(blank=True,null=True)

    twitter = models.URLField(blank=True,null=True)

    #jsut in case 
    contenido = RichTextField()

    imagen = imagen = models.ImageField(upload_to= 'nosotros/', null=False, blank=False,default='articulos/default_img_articulo.jpg')

    def __str__(self):
        return f"Información de Contacto"
    
    def get_absolute_url(self):
        return reverse_lazy('contacto:path_contacto_main')