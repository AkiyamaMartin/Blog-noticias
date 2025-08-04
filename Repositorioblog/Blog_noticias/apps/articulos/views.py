from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from .models import Articulo
from .forms import FormularioCrearArticulo

from categorias.models import Categoria, TipoCategoria

from comentarios.forms import ComentarioForm

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin




def lista_articulos(request, categoria_slug=None): #puede tener o no una categoria articulos/cat 
    todos_los_articulos = Articulo.objects.all().order_by('-creado') # *** nuevos primero

    categoria_actual = None
    if categoria_slug: #si categoriaslug tiene un valor,  
        categoria_actual = get_object_or_404(Categoria, slug=categoria_slug) #busca cat o da error404
        todos_los_articulos = todos_los_articulos.filter(categoria=categoria_actual) #filtra todos los art con current cat

    ordenar_por = request.GET.get('order_by', 'newest')
    if ordenar_por == 'oldest':
        todos_los_articulos = todos_los_articulos.order_by('creado') #viejos primero
    else:
        todos_los_articulos = todos_los_articulos.order_by('-creado') #nuevos

    articulos_por_pagina = 12
    paginator = Paginator(todos_los_articulos,articulos_por_pagina) #le doy todos los art, luego cuantos quiero por pag

    page_number = request.GET.get('page') #obtiene el numero de pag de la url y si no hay es la primera
    page_obj = paginator.get_page(page_number) #Obtenemos el objeto Page (una parte de la lista de art para la página actual)

    
    contexto = {
        'page_obj': page_obj,
        'categoria_actual': categoria_actual,
        'ordenar_por': ordenar_por, 
    }

    return render(request, 'articulos/lista_articulos.html', contexto)


def detalle_articulo(request, articulo_slug):
    articulo = get_object_or_404(Articulo, slug=articulo_slug)

    comentarios = articulo.comentarios.all()
    form_comentario = ComentarioForm()

    

    contexto = {
        'articulo': articulo,
        'comentarios':comentarios,
        'form_comentario': form_comentario,
    }

    return render(request, 'articulos/detalle_articulo.html', contexto)


class CrearArticulo(LoginRequiredMixin,UserPassesTestMixin,CreateView):
    model = Articulo
    template_name = 'articulos/crear_articulo.html'
    form_class = FormularioCrearArticulo
    success_url = reverse_lazy('articulos:path_lista_articulos')

    def test_func(self):
        return self.request.user.is_staff

class EditarArticulo(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Articulo
    template_name = 'articulos/editar_articulo.html'
    form_class = FormularioCrearArticulo
    slug_url_kwarg = 'articulo_slug' # slug en lhgar de pk ///
    context_object_name = 'articulo' #el objeto en el contexto del template 
    def get_success_url(self):
        return reverse_lazy('articulos:path_detalle_articulo', kwargs={'articulo_slug': self.object.slug}) # self.object.slug = el slug del art que se edito
    def test_func(self):
        return self.request.user.is_staff

    

class BorrarArticulo(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Articulo
    template_name = 'articulos/borrar_articulo.html'
    success_url = reverse_lazy('articulos:path_lista_articulos')
    slug_url_kwarg = 'articulo_slug'
    context_object_name = 'articulo'
    
    def test_func(self):
        return self.request.user.is_staff
