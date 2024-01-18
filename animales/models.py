from django.db import models

# Create your models here.
class Animal(models.Model):
    # duenio = models.CharField(max_legth= 50)
    nombre = models.CharField(max_length=30, blank= True, null = True)
    nacimiento = models.DateField(blank= True, null = True)
    vacunacion= models.BooleanField(blank = True)
    desparasitado = models.BooleanField(blank = True)
    observaciones = models.TextField(blank= True, null = True)
    
    
    def calcular_edad(self):
        import datetime
        today = datetime.date.today()
        edad_anios = today.year - self.nacimiento.year
        edad_meses = (today.year - self.nacimiento.year) * 12 + today.month - self.nacimiento.month
        return {'anios': edad_anios, 'meses': edad_meses}
    
    
class Perro(Animal):
    raza = models.CharField(max_length=50, null=True)
    
    def __str__(self) -> str:
        return f"Nombre del Perro: {self.nombre} Nombre del dueño: {...}"
    
    
class Gato(Animal):
    color_pelo = models.CharField(max_length=30,null=True)
    color_ojos = models.CharField(max_length=30, null=True)

    def __str__(self) -> str:
        return f"Nombre del Gato: {self.nombre} Nombre del dueño: {...}"
    
    