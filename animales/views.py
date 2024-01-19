from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.urls import reverse_lazy
from .models import *
from .forms import *
from django.views.generic import ListView,CreateView,DetailView,UpdateView,DeleteView


def padre(request):
    return render(request,'animales/padre.html')

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

class PerroUpdate(UpdateView):
    model = Perro
    form_class = PerroForm
    success_url = reverse_lazy("animales:perrolist")

class PerroDelete(DeleteView):
    model = Perro
    success_url = reverse_lazy("animales:inicio")
