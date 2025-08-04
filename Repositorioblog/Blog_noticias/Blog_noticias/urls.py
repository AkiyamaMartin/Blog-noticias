
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views




from . import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name = 'path_home'),
    
    path('cultura/', include('articulos.urls')),

    path('ckeditor/', include('ckeditor_uploader.urls')),

    path('comentarios/', include('comentarios.urls')),
    
    path('usuarios/', include('usuarios.urls')),



]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
