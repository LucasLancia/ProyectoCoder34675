from django.db import models

class Curso(models.Model):
    nombre=models.CharField(max_length=40)
    camada=models.IntegerField(unique=True)

def __str__(self):
    return f"curso: {self.nombre}, Camada: {self.camada}"

class Estudiantes(models.Model):
    nombre=models.CharField(max_length=40)
    apellido:models.CharField(max_length=40)
    email=models.EmailField()

class Profesor(models.Model):
    nombre=models.CharField(max_length=40)
    apellido:models.CharField(max_length=40)
    email=models.EmailField()
    profesion= models.CharField(max_length=40)

    def __str__(self):
        return f"Profesor: {self.nombre} {self.apellido}"
