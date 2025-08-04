
from django import forms
from .models import Comentario

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['contenido']
        labels = {
            'contenido': 'Tu comentario',
        }

        widgets = {
            'contenido': forms.Textarea(attrs= {'rows': 4, 'placeholder': 'Escribí tu comentario aquí...'}),
            
        }