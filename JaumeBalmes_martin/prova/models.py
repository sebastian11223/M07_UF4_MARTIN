from django.db import models

class Profesores(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    age = models.IntegerField()
    asignatura = models.CharField(max_length=50)
    
class Alumnos(models.Model):
   id = models.AutoField(primary_key=True)
   name = models.CharField(max_length=50)
   surname = models.CharField(max_length=50)
   age = models.IntegerField()
   clase = models.IntegerField()


class Person(models.Model):
    id = models.AutoField(primary_key=True)
    first_Name = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    age = models.IntegerField()
