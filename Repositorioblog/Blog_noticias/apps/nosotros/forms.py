from django import forms
from .models import Nosotros


class FormularioCrearNosotros(forms.ModelForm):

    class Meta:
        model = Nosotros
        fields = ['titulo', 'contenido', 'imagen']

