from django.shortcuts import redirect, render

from . import models
from . import forms


def categoria_list(request):
    consulta = request.GET.get("consulta")
    if consulta:
        categorias = models.Categoria.objects.filter(nombre__contains=consulta)
    else:
        categorias = models.Categoria.objects.all()
    return render(request, "producto/categoria_list.html", {"categorias": categorias})


def categoria_detail(request, pk: int):
    categoria = models.Categoria.objects.get(id=pk)
    return render(request, "producto/categoria_detail.html", {"categoria": categoria})


def categoria_delete(request, pk: int):
    categoria = models.Categoria.objects.get(id=pk)
    contexto = {"categoria": categoria}
    return render(request, "producto/categoria_detail.html", contexto)


def categoria_create(request):
    if request.method == "GET":
        form = forms.CategoriaForm()
    if request.method == "POST":
        form = forms.CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("producto:lista")
    return render(request, "producto/categoria_create.html", {"form": form})
