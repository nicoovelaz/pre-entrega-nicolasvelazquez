from django.urls import path
from mispeliculas import views

urlpatterns = [
    path('', views.inicio ),
    path('formulario/',views.formulario),
    path('busqueda/',views.busqueda),
]