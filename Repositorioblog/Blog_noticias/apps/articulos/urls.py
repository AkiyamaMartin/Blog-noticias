from django.urls import path
from . import views

app_name = 'articulos'

urlpatterns = [
    path('', views.lista_articulos, name='path_lista_home'),

    path('cultura', views.lista_articulos, name = 'path_lista_articulos'),

    path('categoria/<slug:categoria_slug>/', views.lista_articulos, name = 'path_lista_articulos_categoria'),

    path('articulo/<slug:articulo_slug>/', views.detalle_articulo, name='path_detalle_articulo'),

    path('crear/', views.CrearArticulo.as_view(), name='path_crear_articulo'),
  
    path('<slug:articulo_slug>/editar/', views.EditarArticulo.as_view(), name='path_editar_articulo'),

    path('<slug:articulo_slug>/borrar/', views.BorrarArticulo.as_view(), name='path_borrar_articulo'),

    
    

]