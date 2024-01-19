from django import forms
from .models import *

class PerroForm (forms.ModelForm):
    class Meta:
        model = Perro
        fields = "__all__"

class GatoForm (forms.ModelForm):
    class Meta:
        model = Gato
        fields= "__all__"
