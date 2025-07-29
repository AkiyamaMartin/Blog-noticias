from django.urls import path
from . import views

app_name = 'articulos'

urlpatterns = [
    path('', views.lista_articulos, name='path_lista_articulos'),

    path('<slug:articulo_slug>/', views.detalle_articulo, name='path_detalle_articulo'),

    path('cultura', views.lista_articulos, name = 'path_lista_articulos')

]