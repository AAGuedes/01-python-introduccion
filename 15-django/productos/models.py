from django.db import models


class Categoria(models.Model):
    nombre = models.CharField(max_length=255)


class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    stock = models.IntegerField()
    puntaje = models.FloatField()
    # CASCADE: Elimina el producto
    # PROTECT: Lanza un error
    # RESTRICT: Solo elimina si no existen productos
    # SET_NULL: Actualiza a valor nulo
    # SET_DEFAULT: Asigna valor por defecto
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE
    )
