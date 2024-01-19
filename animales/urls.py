
from django.contrib import admin
from django.urls import path
from . import views

app_name = 'animales'

urlpatterns = [
    path('admin/', admin.site.urls),
    path ('',views.padre, name= 'inicio'),
    path ('perro/',views.perro, name= 'perro'),
    path('publicarperro/list/', views.PerroList.as_view(), name= 'perrolist'),
    path('publicarperro/create/', views.PerroCreate.as_view(), name= 'perroform'),
    path('publicarperro/detail/<int:pk>', views.PerroDetail.as_view(), name= 'perro_detail'),
    path('publicarperro/update/<int:pk>', views.PerroUpdate.as_view(), name= 'perro_update'),
    path('publicarperro/delete/<int:pk>', views.PerroDelete.as_view(), name= 'perro_delete'),

]
