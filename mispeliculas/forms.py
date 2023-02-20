from django import forms


class SerieFormulario(forms.Form):
    titulo = forms.CharField()
    genero = forms.CharField()