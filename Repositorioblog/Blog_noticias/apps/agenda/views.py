from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Evento
from .forms import FormularioCrearEvento
from categorias.models import Categoria
from datetime import date, timedelta




def lista_eventos(request, categoria_slug=None, colectividad_slug=None):
    todos_los_eventos = Evento.objects.all().order_by('-creado')
    
    categoria_actual = None
    colectividad_actual = None

    if categoria_slug:
        categoria_actual = get_object_or_404(Categoria, slug=categoria_slug)
        todos_los_eventos = todos_los_eventos.filter(categoria=categoria_actual)
    elif colectividad_slug:
        colectividad_actual = get_object_or_404(Categoria, slug=colectividad_slug)
        todos_los_eventos = todos_los_eventos.filter(colectividad=colectividad_actual)

    ver_pasado = request.GET.get('ver_pasado', 'false') == 'true'
    if not ver_pasado:
        ayer = date.today() - timedelta(days=1)
        todos_los_eventos = todos_los_eventos.filter(fecha__gte=ayer)


    ordenar_por = request.GET.get('order_by', 'newest')
    if ordenar_por == 'oldest':
        todos_los_eventos = todos_los_eventos.order_by('fecha')
    else:
        todos_los_eventos = todos_los_eventos.order_by('-fecha')

    eventos_por_pagina = 6
    paginator = Paginator(todos_los_eventos, eventos_por_pagina)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    contexto = {
        'page_obj': page_obj,
        'categoria_actual': categoria_actual,
        'colectividad_actual': colectividad_actual,
        'ordenar_por': ordenar_por,
        'ver_pasado': ver_pasado,
    }

    return render(request, 'agenda/lista_eventos.html', contexto)


def detalle_evento(request, evento_slug):
    evento = get_object_or_404(Evento, slug=evento_slug)

    

    contexto = {
        'evento': evento,
        'user_ya_voto': evento.asistentes.filter(id=request.user.id).exists() if request.user.is_authenticated else False,
        'can_assist': evento.fecha >= date.today(),
        
    }

    return render(request, 'agenda/detalle_evento.html', contexto)



class CrearEvento(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Evento
    template_name = 'agenda/crear_evento.html'
    form_class = FormularioCrearEvento
    success_url = reverse_lazy('agenda:path_lista_eventos')

    def test_func(self):
        return self.request.user.is_staff

class EditarEvento(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Evento
    template_name = 'agenda/editar_evento.html'
    form_class = FormularioCrearEvento
    slug_url_kwarg = 'evento_slug'
    context_object_name = 'evento'
    
    def get_success_url(self):
        return reverse_lazy('agenda:path_detalle_evento', kwargs={'evento_slug': self.object.slug})

    def test_func(self):
        return self.request.user.is_staff

class BorrarEvento(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Evento
    template_name = 'agenda/borrar_evento.html'
    success_url = reverse_lazy('agenda:path_lista_eventos')
    slug_url_kwarg = 'evento_slug'
    context_object_name = 'evento'
    
    def test_func(self):
        return self.request.user.is_staff
    


    

class AsistirEvento(LoginRequiredMixin, View):
    def post(self, request, evento_slug):
        evento = get_object_or_404(Evento, slug=evento_slug)
        if evento.fecha >= date.today() and not evento.asistentes.filter(id=request.user.id).exists():
            evento.asistencias += 1
            evento.asistentes.add(request.user)
            evento.save()
        return reverse_lazy('agenda:path_detalle_evento', evento_slug=evento.slug)