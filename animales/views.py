from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.urls import reverse_lazy
from .models import *
from .forms import *
from django.views.generic import ListView,CreateView,DetailView,UpdateView,DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
#-----------------------------------Inicio----------------------------------------------------------

def padre(request):
    return render(request,'animales/padre.html')
def nosotros(request):
    return render(request,'animales/nosotros.html')
#------------------------------Vistas para Perro--------------------------------------------
@login_required
def perro (request):
    return render(request, 'animales/perro.html')

class PerroCreate(CreateView):
    model = Perro
    form_class = PerroForm
    success_url = reverse_lazy("animales:perro")

class PerroList(ListView):
    model = Perro
    template_name = 'animales/perro_list.html'

    def get_queryset(self):
        if self.request.GET.get('consulta'):
            consultar = self.request.GET.get('consulta')
            object_list= Perro.objects.filter(nombre__icontains= consultar)
        else:
            object_list= Perro.objects.all()
        return object_list
class PerroDetail(DetailView):
    model = Perro


class PerroUpdate(LoginRequiredMixin,UpdateView):
    model = Perro
    form_class = PerroForm
    success_url = reverse_lazy("animales:perrolist")

class PerroDelete(LoginRequiredMixin,DeleteView):
    model = Perro
    success_url = reverse_lazy("animales:inicio")

#--------------------------------Vistas para Gato---------------------------------
@login_required
def gato (request):
    return render(request, 'animales/gato.html')

class GatoCreate(CreateView):
    model = Gato
    form_class = GatoForm
    success_url = reverse_lazy("animales:gato")

class GatoList(ListView):
    model = Gato
    template_name = 'animales/gato_list.html'

    def get_queryset(self):
        if self.request.GET.get('consulta'):
            consultar = self.request.GET.get('consulta')
            object_list= Gato.objects.filter(nombre__icontains= consultar)
        else:
            object_list= Gato.objects.all()
        return object_list
class GatoDetail(DetailView):
    model = Gato

class GatoUpdate(LoginRequiredMixin,UpdateView):
    model = Gato
    form_class = GatoForm
    success_url = reverse_lazy("animales:gato_list")

class GatoDelete(LoginRequiredMixin,DeleteView):
    model = Gato
    success_url = reverse_lazy("animales:inicio")



