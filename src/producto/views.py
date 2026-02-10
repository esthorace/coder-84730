from django.shortcuts import render

from . import models


def categoria_list(request):
    categorias = models.Categoria.objects.all()
    return render(request, "producto/categoria_list.html", {"categorias": categorias})


def categoria_detail(request, pk: int):
    categoria = models.Categoria.objects.get(id=pk)
    contexto = {"categoria": categoria}
    return render(request, "producto/categoria_detail.html", contexto)


def categoria_delete(request, pk: int):
    categoria = models.Categoria.objects.get(id=pk)
    contexto = {"categoria": categoria}
    return render(request, "producto/categoria_detail.html", contexto)
