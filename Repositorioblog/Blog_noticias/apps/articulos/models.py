from django.db import models
# from django.contrib.auth.models import User # Descomentar cuando tengas el modelo User (después de python manage.py migrate inicial)
# from categorias.models import Categoria   # Descomentar cuando hayas creado tu app 'categorias' y su modelo Categoria
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse
from categorias.models import Categoria
# Create your models here.

class Articulo(models.Model):
    creado = models.DateTimeField(auto_now_add=True)

    modificado = models.DateTimeField(auto_now=True)

    titulo = models.CharField(max_length=150)

    slug = models.SlugField(max_length=150, unique=True, blank=True, help_text="Slug para la URL del artículo, se genera automáticamente.")
    #https://docs.djangoproject.com/en/5.0/ref/urls/#path-converters
    
    autor = models.CharField(max_length=30)
    #autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articulos_creados') 
    

    descripcion = models.CharField(max_length=300) #resumen para mostrar en el home

    contenido = RichTextUploadingField()

    imagen = models.ImageField(upload_to= 'articulos/', null=False, blank=False,default='articulos/default_img_articulo.jpg')

    comentarios_habilitados = models.BooleanField(default=True)

    visitas = models.IntegerField(default=0)

    likes = models.IntegerField(default=0)

    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True, related_name='articulos')



    # NUEVO CAMPO DE AUTOR
    # on_delete=models.CASCADE significa que si el usuario se borra, sus artículos también se borrarán.
    # related_name='articulos' permite acceder a los artículos de un usuario: usuario.articulos.all()


    #Los puse así inicialmente para que puedas realizar la migración sin problemas si ya tienes artículos creados. 
    # Una vez que hayas asignado autores a tus artículos existentes, podrías considerar cambiarlos a null=False, blank=False 
    # si quieres que el autor sea obligatorio para todos los futuros artículos.
    #autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articulos', null=True, blank=True)

    
    

    

    class Meta:
        ordering = ['-creado'] # Ordena MAS nuevo primero
        verbose_name_plural = "Artículos" # para que se vea mejor en eo panel admin, sino adivina el plural

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


