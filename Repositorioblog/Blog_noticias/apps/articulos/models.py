from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse
from categorias.models import Categoria
from django.contrib.auth.models import User
# Create your models here.

class Articulo(models.Model):
    creado = models.DateTimeField(auto_now_add=True)

    modificado = models.DateTimeField(auto_now=True)

    titulo = models.CharField(max_length=150)

    slug = models.SlugField(max_length=150, unique=True, blank=True, help_text="Slug para la URL del artículo, se genera automáticamente.")
    #https://docs.djangoproject.com/en/5.0/ref/urls/#path-converters
    
    colectividad = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True, related_name='colectividad')
    
    autor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='articulos_creados')

    descripcion = models.CharField(max_length=300) #resumen para mostrar en el home

    contenido = RichTextUploadingField()
    
    imagen = models.ImageField(upload_to= 'articulos/', null=False, blank=False,default='articulos/default_img_articulo.jpg')

    comentarios_habilitados = models.BooleanField(default=True)

    visitas = models.IntegerField(default=0)

    likes = models.IntegerField(default=0)

    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True, related_name='articulos')

    youtube_url = models.URLField(blank=True, null=True)
 

    

    class Meta:
        ordering = ['-creado'] # Ordena MAS nuevo primero
        

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
            return reverse('articulos:path_detalle_articulo', kwargs={'articulo_slug': self.slug})


