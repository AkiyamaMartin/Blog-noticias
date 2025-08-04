from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden #accesos no autorizados

from articulos.models import Articulo
from .models import Comentario
from .forms import ComentarioForm


@login_required #decorador
def add_comentario(request,  articulo_slug):
    articulo = get_object_or_404(Articulo, slug=articulo_slug)

    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.articulo = articulo
            comentario.autor = request.user
            comentario.save()
        return redirect('articulos:detalle_articulo', slug=articulo.slug)
        


    
@login_required
def edit_comentario(request, articulo_slug, comentario_id):
    comentario = get_object_or_404(Comentario, id=comentario_id)

    if request.user != comentario.autor:
        return HttpResponseForbidden('Solo el autor puede editar su comentario.')
    
    if request.method == 'POST':
        form = ComentarioForm(request.POST, instance=comentario)
        if form.is_valid():
            form.save()
            return redirect('articulos:path_detalle_articulo', articulo_slug=comentario.articulo.slug)
        
    else:
        form = ComentarioForm(instance=comentario)
        
    return render(request, 'comentarios/edit_comentario.html', {'form': form, 'comentario': comentario})

@login_required
def delete_comentario(request, articulo_slug, comentario_id):
    comentario = get_object_or_404(Comentario, id=comentario_id)

    if request.user != comentario.autor and not request.user.is_staff:
        return HttpResponseForbidden('Solo el autor puede eliminar su comentario')
    
    if request.method == 'POST':
        comentario.delete()
        return redirect('articulos:path_detalle_articulo', articulo_slug=comentario.articulo.slug)
    
    return render(request, 'comentarios/confirm_delete_comentario.html', {'comentario':comentario})
    