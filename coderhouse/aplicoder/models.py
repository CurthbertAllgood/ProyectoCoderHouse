from django.db import models

# Create your models here.
class equipos(models.Model):
    club=models.CharField(max_length=30)
    pais=models.CharField(max_length=30)

class jugador(models.Model):
    nombre=models.CharField(max_length=30)
    posicion=models.CharField(max_length=30)
    numero=models.IntegerField()

class selecciones(models.Model):
    pais=models.CharField(max_length=30)
    continente=models.CharField(max_length=20)
    

class Familia(models.Model):
    nombre=models.CharField(max_length=40)
    DNI=models.IntegerField()

