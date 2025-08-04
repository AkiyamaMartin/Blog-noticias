from django.db import models
from articulos.models import Articulo

from django.contrib.auth import get_user_model


User = get_user_model()

class Comentario(models.Model):
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE, related_name='comentarios')
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comentarios')
    contenido = models.TextField(max_length=500)
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['creado']
    
    def __str__(self):
        return f'Comentario de {self.autor.username} en {self.articulo.titulo[:30]}' #toma los primeros 30char del titulo
    