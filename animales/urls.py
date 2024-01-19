
from django.contrib import admin
from django.urls import path
from . import views

app_name = 'animales'

urlpatterns = [
    path('admin/', admin.site.urls),
    path ('',views.padre, name= 'inicio'),
    #-----------------------------------PERRO---------------------------------------------
    path ('perro/',views.perro, name= 'perro'),
    path('publicarperro/list/', views.PerroList.as_view(), name= 'perrolist'),
    path('publicarperro/create/', views.PerroCreate.as_view(), name= 'perroform'),
    path('publicarperro/detail/<int:pk>', views.PerroDetail.as_view(), name= 'perro_detail'),
    path('publicarperro/update/<int:pk>', views.PerroUpdate.as_view(), name= 'perro_update'),
    path('publicarperro/delete/<int:pk>', views.PerroDelete.as_view(), name= 'perro_delete'),
    #------------------------------------GATO---------------------------------------------
    path('gato/', views.gato,name='gato'),
    path('publicargato/create/', views.GatoCreate.as_view(), name= 'gato_form'),
    path('publicargato/list/', views.GatoList.as_view(), name= 'gato_list'),
    path('publicargato/detail/<int:pk>', views.GatoDetail.as_view(), name= 'gato_detail'),
    path('publicargato/update/<int:pk>', views.GatoUpdate.as_view(), name= 'gato_update'),
    path('publicargato/delete/<int:pk>', views.GatoDelete.as_view(), name= 'gato_delete'),

]
