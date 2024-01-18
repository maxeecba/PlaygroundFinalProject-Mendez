
from django.contrib import admin
from django.urls import path
from . import views

app_name = 'animales'

urlpatterns = [
    path('admin/', admin.site.urls),
    path ('',views.padre, name= 'inicio'),
    path ('perro/',views.perro, name= 'perro'),
    path('publicarperro/List/', views.PerroList.as_view(), name= 'perrolist'),
    path('publicarperro/create/', views.PerroCreate.as_view(), name= 'perroform')
    
]
