from django.urls import path
from . import views

app_name = 'agenda'

urlpatterns = [
    path('', views.lista_eventos, name='path_lista_eventos'),

    path('categoria/<slug:categoria_slug>/', views.lista_eventos, name = 'path_lista_eventos_categoria'),

    path('colectividad/<slug:colectividad_slug>/', views.lista_eventos, name='path_lista_eventos_colectividad'),    
    
    path('evento/<slug:evento_slug>/', views.detalle_evento, name='path_detalle_evento'),

    path('crear/', views.CrearEvento.as_view(), name='path_crear_evento'),

    path('<slug:evento_slug>/editar/', views.EditarEvento.as_view(), name='path_editar_evento'),
    
    path('<slug:evento_slug>/borrar/', views.BorrarEvento.as_view(), name='path_borrar_evento'),



]