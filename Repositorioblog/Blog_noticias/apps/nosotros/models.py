from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse
from categorias.models import Categoria
from django.contrib.auth.models import User


class Nosotros(models.Model):
    creado = models.DateTimeField(auto_now_add=True)

    modificado = models.DateTimeField(auto_now=True)

    titulo = models.CharField(max_length=40)

    slug = models.SlugField(max_length=50, unique=True, blank=True, help_text="se genera automáticamente.")

    contenido = RichTextUploadingField()

    imagen = models.ImageField(upload_to= 'nosotros/', null=False, blank=False,default='articulos/default_img_articulo.jpg')

    class Meta:
        ordering = ['creado'] #mas viejo primero 

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
                self.slug = f"{original_slug}--{num}"
                num += 1
        super().save(*args,**kwargs)
    
    def get_absolute_url(self):
        return reverse('nosotros:path_detalle_nosotros', kwargs={'nosotros_slug': self.slug})
    
    def __str__(self):
        return self.titulo

