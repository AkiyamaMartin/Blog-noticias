from django.urls import path

from django.contrib.auth import views as auth

from . import views

app_name = 'usuarios'



urlpatterns = [
    path('login/', auth.LoginView.as_view(template_name='usuarios/login.html'),name = 'path_login'),

    path('logout/', auth.LogoutView.as_view(),name = 'path_logout'),

    path('registro/',views.RegistroUsuario.as_view(), name = 'path_registro'),
]

    