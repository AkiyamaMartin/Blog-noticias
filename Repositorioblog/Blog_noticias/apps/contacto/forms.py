from django import forms

class FormularioContacto(forms.Form):
    nombre = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={'placehoder': 'Tu nombre'}),
        label='Nombre',
        required=True
    )
    
    email = forms.EmailField(
        widget=forms.TextInput(attrs={'placeholder': 'Tu email'}),
        label='Email',
        required=True
    )

    asunto = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={'placeholder': 'Asunto'}),
        label='Asunto',
        required=True
    )

    mensaje = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Tu mensaje'}),
        label='Mensaje',
        required=True
    )
