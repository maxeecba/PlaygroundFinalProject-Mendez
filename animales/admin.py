from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Animal)
admin.site.register(models.Perro)
admin.site.register(models.Gato)