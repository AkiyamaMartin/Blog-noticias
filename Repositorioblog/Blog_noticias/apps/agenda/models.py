from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse
from categorias.models import Categoria
from django.contrib.auth.models import User


# Create your models here.


class Evento(models.Model):
    creado = models.DateTimeField(auto_now_add=True)

    modificado = models.DateTimeField(auto_now=True)

    titulo = models.CharField(max_length=150)

    slug = models.SlugField(max_length=150, unique=True, blank=True, help_text="Se genera automáticamente.")

    fecha = models.DateField()

    hora = models.TimeField(null=True,blank=True)

    lugar = models.CharField(max_length=250)

    entrada = models.CharField(max_length=150, null=True,blank=True)

    google_maps_url = models.URLField(max_length=500, blank=True)

    colectividad = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True, related_name='colectividad_eventos')

    autor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='eventos_creados')

    descripcion = models.CharField(max_length=300) #resumen para mostrar bajo imagen

    contenido = RichTextUploadingField()

    imagen = models.ImageField(upload_to= 'agenda/', null=False, blank=False,default='articulos/default_img_articulo.jpg')
    #flyer
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True, related_name='agenda')

    class Meta: 
        ordering = ['-creado']
    
    def __str__(self):
        return self.titulo
    
    def save(self, *args, **kwargs): 
        from django.utils.text import slugify
        if not self.slug: 
            self.slug = slugify(self.titulo)
            
            original_slug = self.slug
            Klass = self.__class__
            num = 1
            
            while Klass.objects.filter(slug=self.slug).exists():
                self.slug = f"{original_slug}-{num}"
                num += 1
        super().save(*args, **kwargs)


    def get_absolute_url(self):
            return reverse('agenda:path_detalle_evento', kwargs={'evento_slug': self.slug})

