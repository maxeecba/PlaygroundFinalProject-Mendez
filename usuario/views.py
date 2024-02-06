from django.contrib.auth.views import LoginView
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .forms import *


#----------------------------------OPCIONES-----------------------------
def opciones(request):
    return render(request,"usuario/opciones.html")

# ----------------------------------LOGIN-------------------------------------------

class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = "usuario/login.html"

#----------------------------------REGISTER------------------------------------------
def register(request):
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render (request, 'usuario/login.html')
        else:
            form = CustomUserCreationForm()
    return render(request,'usuario/register.html', {'form': form})