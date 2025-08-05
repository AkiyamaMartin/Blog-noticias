from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Nosotros
from .forms import FormularioCrearNosotros

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin



# Create your views here.





def lista_nosotros(request):
    todos_los_nosotros = Nosotros.objects.all().order_by('creado')

    about_principal = todos_los_nosotros.first() #tengo que crear primero el principal we

    colectividades = todos_los_nosotros.exclude(pk=about_principal.pk)

    contexto = {
        'about_principal': about_principal,
        'colectividades': colectividades,
    }

    return render(request, 'nosotros/nosotros_main.html', contexto)

def detalle_nosotros(request, nosotros_slug):
    nosotros = get_object_or_404(Nosotros, slug=nosotros_slug)

      
    contexto = {
        'nosotros': nosotros,
        }

    return render(request, 'nosotros/detalle_nosotros.html', contexto)

class CrearNosotros(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Nosotros
    template_name = 'nosotros/crear_nosotros.html'
    form_class = FormularioCrearNosotros
    success_url = reverse_lazy('nosotros:path_nosotros_main')

    def test_func(self):
        return self.request.user.is_staff
    
class EditarNosotros(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Nosotros
    template_name = 'nosotros/editar_nosotros.html'
    form_class = FormularioCrearNosotros
    slug_url_kwarg = 'nosotros_slug'
    context_object_name = 'nosotros'
    def get_success_url(self):
        return reverse_lazy('nosotros:path_detalle_nosotros', kwargs={'nosotros_slug': self.object.slug})
    def test_func(self):
        return self.request.user.is_staff
    
class BorrarNosotros(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model = Nosotros
    template_name = 'nosotros/borrar_nosotros.html'
    success_url = reverse_lazy('nosotros:path_nosotros_main')
    slug_url_kwarg = 'nosotros_slug'
    context_object_name = 'nosotros'

    def test_func(self):
        return self.request.user.is_staff