from django.shortcuts import render
from django.http import HttpResponse
from mispeliculas.models import *
from .forms import SerieFormulario
# Create your views here.

def inicio(request):
    return render(request,'mispeliculas/inicio.html')
def busqueda(request):
    return render(request,'mispeliculas/busqueda.html')
def formulario(request):
    miFormulario = SerieFormulario()
    if request.method == 'POST':
        miFormulario= SerieFormulario(request.POST)
        if miFormulario.is_valid():
            print("valido")
            serie = Serie()
            serie.titulo = miFormulario.cleaned_data['titulo']
            serie.genero = miFormulario.cleaned_data['genero']
            serie.temporadas = miFormulario.cleaned_data['temporadas']
            serie.save()
        else:
            print("No VALIDO")    
        
    else:
        miFormulario = SerieFormulario()
        
    return render(request, "mispeliculas/formulario.html", {"miFormulario":miFormulario})       

def busquedaSerie(request):
    return render(request, "mispeliculas/busqueda.html")

def buscar(request):  
    if request.GET["titulo"]:
        titulo = request.GET['titulo']
        serie = Serie.objects.filter(titulo__icontains=titulo)
        #temporadas = Serie.objects.filter(temporadas__icontains=temporadas)
        return render(request, "mispeliculas/resbusqueda.html", { "titulo":serie})
    else:
        respuesta = "No ingresaste datos"
    return HttpResponse(respuesta)