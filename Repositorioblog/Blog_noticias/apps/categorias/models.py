from django.db import models
from django.utils.text import slugify
from django.urls import reverse


# Create your models here.
class TipoCategoria(models.Model):
    nombre = models.CharField(max_length=20, unique=True, help_text="Ej: Artículo, Evento, Galeria")
    slug = models.SlugField(max_length=25, unique=True, blank=True)

    class Meta:
        ordering = ['nombre'] #alfabeticamente en el amdin
    
    def save(self, *args, **kwargs):
        if not self.slug: #generamo slug con el nombre 
            self.slug = slugify(self.nombre)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.nombre
    

class Categoria(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=30, unique=True, blank=True)

    #R many to many categoria con tipocategoria

    tipos = models.ManyToManyField(
        TipoCategoria,
        related_name='categorias',
        blank=True, #puede no tener un tipo asociado cuando se crea
        help_text="Seleccioná los tipos a los que pertenece esta categoría (Ej: Artículo, Evento, Galeria)"
        
    )

    class Meta:
        ordering = ['nombre']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nombre)
        super().save(*args,**kwargs)
    
    def __str__(self):
        tipos_str = ", ".join([t.nombre for t in self.tipos.all()])
        return f"{self.nombre} ({tipos_str})" if tipos_str else self.nombre
    
    def get_absolute_url(self):
        return reverse('articulos:path_lista_articulos_categoria', kwargs={'categoria_slug': self.slug})
        