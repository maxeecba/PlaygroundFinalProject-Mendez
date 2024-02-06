
from django.contrib import admin
from django.urls import path
from . import views
#----------Logout----------------
from django.contrib.auth.views import LogoutView

app_name = 'usuario'

urlpatterns = [
    path('admin/', admin.site.urls),
#-------------------------------------LOGIN-----------------------------------------------
    path('login/',views.CustomLoginView.as_view(), name= 'login' ),
    # path('index/',views.index, name= 'login' ),
    # path('register/', views.register,name='register'),
    path('opciones/',views.opciones, name='opciones'),
    path('bienvenida/',views.bienvenida, name='bienvenida'),
    path('logout/', LogoutView.as_view(template_name = 'usuario/logout.html'), name= 'logout'),
    path('register/', views.register, name= 'register'),

]
