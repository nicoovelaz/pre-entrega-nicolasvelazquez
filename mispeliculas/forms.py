from django import forms
from .models import Serie



class SerieFormulario(forms.Form):
    titulo = forms.CharField(max_length=100)
    genero = forms.CharField(max_length=100)
    temporadas= forms.IntegerField(min_value=1) 