from django import forms
from .models import Evento
from categorias.models import Categoria, TipoCategoria

class FormularioCrearEvento(forms.ModelForm):
    
    class Meta:
        model = Evento
        fields = ['titulo', 'descripcion', 'contenido', 'imagen', 'categoria', 'colectividad', 'fecha', 'hora', 'lugar', 'entrada', 'google_maps_url']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['categoria'].queryset = Categoria.objects.filter(tipos__nombre='Agenda')
        self.fields['categoria'].empty_label = "Selecciona una categoría"
        self.fields['categoria'].required = False
        
        self.fields['colectividad'].queryset = Categoria.objects.filter(tipos__nombre='Colectividad')
        self.fields['colectividad'].empty_label = "Selecciona una colectividad"
        self.fields['colectividad'].required = False
        
        self.fields['fecha'].widget.attrs.update({'placeholder': 'DD-MM-AAAA'})