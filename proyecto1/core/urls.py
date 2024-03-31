from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index' ),
    path('categorias/<str:categoria_nombre>', categoria, name='categorias' ),
    path('foro/', foro, name='foro' ),
    path('registro/', registro, name='registro' ),
    path('login/', login, name='login' ),
    path('recuperar/', recuperar, name='recuperar' ),
    path('mi-cuenta/', miCuenta, name='mi-cuenta' ),
]