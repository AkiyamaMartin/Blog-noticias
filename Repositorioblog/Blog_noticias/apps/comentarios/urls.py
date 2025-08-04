from django.urls import path
from . import views

app_name = 'comentarios'


urlpatterns = [
    path('<slug:articulo_slug>/add/', views.add_comentario, name='path_add_comentario'),

    path('<slug:articulo_slug>/<int:comentario_id>/edit/', views.edit_comentario, name='path_edit_comentario'),

    path('<slug:articulo_slug>/<int:comentario_id>/delete/', views.delete_comentario, name='path_delete_comentario'),



    
]