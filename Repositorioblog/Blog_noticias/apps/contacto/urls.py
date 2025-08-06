from django.urls import path
from . import views

app_name = 'contacto'

urlpatterns = [

    path('', views.lista_contacto, name = 'path_contacto_main'),

    #crear, editar, borrar y detalle igual que about us pal futuro

]