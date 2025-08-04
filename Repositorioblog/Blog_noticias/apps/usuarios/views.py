from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import login
from .forms import FormularioRegistro



class RegistroUsuario(CreateView):
    template_name = 'usuarios/registro_usuario.html'
    form_class = FormularioRegistro
    success_url = reverse_lazy('usuarios:path_login')