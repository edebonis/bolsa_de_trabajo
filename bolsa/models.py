from django.db import models
from django.contrib.auth.models import User


class Oportunidad(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=5000)
    visible = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Tipo(models.Model):
    nombre = models.CharField(max_length=50)
    relacionado = models.ManyToManyField(self)