from django.contrib import admin

from .models import Categoria, Producto

admin.site.register(Categoria)

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ("categoria", "nombre", "stock", "unidad_de_medida", "precio")
    list_filter = ("categoria", "unidad_de_medida")
    search_fields = ("nombre", "categoria__nombre")