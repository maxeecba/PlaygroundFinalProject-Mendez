from django.contrib.auth.forms import  AuthenticationForm
from django.contrib.auth.models import User
from django import forms



class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        models = User
        fields = ["username", "password"]
        widgets= {
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "password": forms.PasswordInput(attrs={"class":"form-control"}),
        }