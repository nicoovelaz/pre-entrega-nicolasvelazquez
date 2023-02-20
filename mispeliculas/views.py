from django.shortcuts import render
from django.http import HttpResponse
from mispeliculas.models import *
from mispeliculas.forms import SerieFormulario

# Create your views here.

def inicio(request):
    return render(request,'mispeliculas/inicio.html')
def busqueda(request):
    return render(request,'mispeliculas/busqueda.html')
def formulario(request):
    if request.method == 'POST':
        miFormulario = SerieFormulario(request.POST)
        print(miFormulario)
        
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            serie = Serie(titulo=informacion['titulo'], genero=informacion['genero'])
            serie.save()
            return render(request, "mispeliculas/inicio.html") 
        
    else:
        miFormulario = SerieFormulario()
        
    return render(request, "mispeliculas/formulario.html", {"miFormulario":miFormulario})              