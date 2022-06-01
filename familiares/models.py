from django.db import models

class Familiares(models.Model):
    dni= models.IntegerField(unique=True)
    nombre= models.CharField (max_length=10)
    apellido= models.CharField (max_length=10)
    edad= models.IntegerField(blank= True, null=True)
    hijos= models.IntegerField(blank= True, null=True)
    activo= models.BooleanField(default=True)
    