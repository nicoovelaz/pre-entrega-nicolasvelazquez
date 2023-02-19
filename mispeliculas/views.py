from django.shortcuts import render
from django.http import HttpResponse
from mispeliculas.models import *

# Create your views here.

def inicio(request):
    return render(request,'mispeliculas/inicio.html')
def formulario(request):
    return render(request,'mispeliculas/formulario.html')
def busqueda(request):
    return render(request,'mispeliculas/busqueda.html')