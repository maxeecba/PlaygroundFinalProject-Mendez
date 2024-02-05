
from django.contrib import admin
from django.urls import path
from . import views

app_name = 'usuario'

urlpatterns = [
    path('admin/', admin.site.urls),
#-------------------------------------LOGIN-----------------------------------------------
    path('login/',views.CustomLoginView.as_view(), name= 'login' ),
    # path('index/',views.index, name= 'login' ),
    # path('register/', views.register,name='register'),
    path('opciones/',views.opciones, name='opciones'),
    # path('logout/', LogoutView.as_view(template_name = 'usuario/logout.html'), name= 'logout')
]
