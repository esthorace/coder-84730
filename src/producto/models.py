from django.db import models


class Categoria(models.Model):
    nombre = models.CharField(max_length=250, unique=True)
    descripcion = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.nombre}"


class Producto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="categoría")
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(null=True, blank=True)
    unidad_de_medida = models.CharField(max_length=50)
    stock = models.FloatField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_actualizacion = models.DateTimeField(editable=False, auto_now=True)

    def __str__(self) -> str:
        return f"{self.nombre} ({self.unidad_de_medida}) ${self.precio}"
    
    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        constraints = [
            models.UniqueConstraint(fields=["categoria", "nombre"], name="categoria_nombre")
        ]
        indexes = [models.Index(fields=["nombre"])]
        