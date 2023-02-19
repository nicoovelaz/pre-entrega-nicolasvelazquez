from django.shortcuts import render
from django.http import HttpResponse
from mispeliculas.models import *

# Create your views here.

def inicio(request):
    return HttpResponse("vista inicio")
def formulario(request):
    return HttpResponse("vista formulario")
def busqueda(request):
    return HttpResponse("vista busqueda")