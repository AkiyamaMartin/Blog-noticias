from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.core.paginator import Paginator

# Create your views here.

from .models import Articulo

def lista_articulos(request):
    todos_los_articulos = Articulo.objects.all().order_by('-creado') # *** nuevos primero

    articulos_por_pagina = 12
    paginator = Paginator(todos_los_articulos,articulos_por_pagina) #le doy todos los art, luego cuantos quiero por pag

    page_number = request.GET.get('page') #obtiene el numero de pag de la url y si no hay es la primera
    
    page_obj = paginator.get_page(page_number) #Obtenemos el objeto Page (una parte de la lista de art para la página actual)

    contexto = {
        'page_obj': page_obj,
    }

    return render(request, 'articulos/lista_articulos.html', contexto)


def detalle_articulo(request, articulo_slug):
    articulo = get_object_or_404(Articulo, slug=articulo_slug)

    contexto = {
        'articulo': articulo,
    }

    return render(request, 'articulos/detalle_articulo.html', contexto)


