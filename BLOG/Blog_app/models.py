from django.db import models

# Create your models here.


class Materia(models.Model):
    nombre = models.CharField(max_length=40)
    comision = models.IntegerField()
    
    
class Alumno(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    año = models.IntegerField()
    carrera = models.CharField(max_length=35)

class Profesor(models.Model):
    nombre = models.CharField(max_length=35)
    apellido = models.CharField(max_length=35)
    curso = models.CharField(max_length=20)
    

class Examen(models.Model):
    nombre = models.CharField(max_length=35)
    fecha = models.DateField()
    aprobado = models.BooleanField()


    
