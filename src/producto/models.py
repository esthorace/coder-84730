from django.db import models


class Categoria(models.Model):
    nombre = models.CharField(max_length=250, unique=True)
    descripcion = models.TextField(null=True, blank=True)
