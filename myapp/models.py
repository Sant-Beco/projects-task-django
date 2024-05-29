from django.db import models

# Create your models here.

class project(models.Model):
  name = models.CharField(max_length=200)

  def __str__(self):
    return self.name

class Task(models.Model):
  title = models.CharField(max_length=200)
  description = models.TextField()
  project = models.ForeignKey(project, on_delete=models.CASCADE)
  done = models.BooleanField(default=False)

  def __str__(self):
    return self.title + ' - ' + self.project.name

class Actividades(models.Model):
  titulo = models.CharField(max_length=100)
  description = models.CharField(max_length=300)
  nota = models.TextField()

class Estudiante(models.Model):
  nombre = models.CharField(max_length=160)
  apellido = models.TextField()
  edad = models.IntegerField()
  curso = models.TextField()




