from django import forms
from django import forms

class ArticuloForm(forms.Form):
    
    titulo = forms.CharField(max_length=30)
    texto = forms.CharField(max_length=1000)
    fecha = forms.DateField()
    
class AutorForm(forms.Form):
    
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    profesion = forms.DateField(max_length=30)
    
class Seccionform(forms.Form):
    
    titulo = forms.CharField(max_length=30)
    