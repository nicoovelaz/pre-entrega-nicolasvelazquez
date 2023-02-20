from django.urls import path
from mispeliculas import views

urlpatterns = [
    path('', views.inicio, name="inicio" ),
    path('formulario/',views.formulario, name="formulario"),
    path('busqueda/',views.busqueda,name="busqueda"),
]