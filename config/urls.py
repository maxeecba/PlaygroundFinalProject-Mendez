
from django.contrib import admin
from django.urls import path,include
from animales.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('animales.urls'))
]
