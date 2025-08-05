from django.urls import path
from . import views

app_name = 'nosotros'

urlpatterns = [

    path('', views.lista_nosotros, name = 'path_nosotros_main'),

    path('crear/', views.CrearNosotros.as_view(), name='path_crear_nosotros'),

    

    
  
    path('<slug:nosotros_slug>/editar/', views.EditarNosotros.as_view(), name='path_editar_nosotros'),

    path('<slug:nosotros_slug>/borrar/', views.BorrarNosotros.as_view(), name='path_borrar_nosotros'),

    path('<slug:nosotros_slug>/', views.detalle_nosotros, name='path_detalle_nosotros'),
    


]

