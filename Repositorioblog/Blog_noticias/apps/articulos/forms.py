from django import forms
from .models import Articulo
from categorias.models import Categoria, TipoCategoria

class FormularioCrearArticulo(forms.ModelForm):
    
    class Meta:
        model = Articulo
        fields = ['titulo', 'descripcion', 'contenido', 'imagen', 'categoria']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['categoria'].queryset = Categoria.objects.filter(tipos__nombre='Cultura')
        self.fields['categoria'].empty_label = "Selecciona una categoría"
        self.fields['categoria'].required = False
        