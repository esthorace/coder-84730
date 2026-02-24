from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from . import models
from . import forms


# def categoria_list(request):
#     consulta = request.GET.get("consulta")
#     if consulta:
#         categorias = models.Categoria.objects.filter(nombre__contains=consulta)
#     else:
#         categorias = models.Categoria.objects.all()
#     return render(request, "producto/categoria_list.html", {"categorias": categorias})

class CategoriaList(ListView):
    model = models.Categoria
    # template_name = "producto/categoria_list.html"
    # context_object_name = "categorias"

    def get_queryset(self):
        consulta = self.request.GET.get("consulta")
        if consulta:
            categorias = models.Categoria.objects.filter(nombre__contains=consulta)
        else:
            categorias = models.Categoria.objects.all()
        return categorias



# def categoria_detail(request, pk: int):
#     categoria = models.Categoria.objects.get(id=pk)
#     return render(request, "producto/categoria_detail.html", {"categoria": categoria})

class CategoriaDetail(DetailView):
    model = models.Categoria


# def categoria_delete(request, pk: int):
#     categoria = models.Categoria.objects.get(id=pk)
#     if request.method == "POST":
#         categoria.delete()
#         return redirect("producto:lista")
#     contexto = {"categoria": categoria}
#     return render(request, "producto/categoria_confirm_delete.html", contexto)

class CategoriaDelete(DeleteView):
    model = models.Categoria
    success_url = reverse_lazy("producto:lista")

# def categoria_create(request):
#     if request.method == "POST":
#         form = forms.CategoriaForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("producto:lista")
#     else:
#         form = forms.CategoriaForm()
   
#     return render(request, "producto/categoria_create.html", {"form": form})

class CategoriaCreate(CreateView):
    model = models.Categoria
    form_class = forms.CategoriaForm
    success_url = reverse_lazy("producto:lista")


# def categoria_update(request, pk: int):
#     categoria = models.Categoria.objects.get(id=pk)
#     if request.method == "GET":
#         form = forms.CategoriaForm(instance=categoria)
#     if request.method == "POST":
#         form = forms.CategoriaForm(request.POST, instance=categoria)
#         if form.is_valid():
#             form.save()
#             return redirect("producto:lista")
#     return render(request, "producto/categoria_form.html", {"form": form})


class CategoriaUpdate(UpdateView):
    model = models.Categoria
    form_class = forms.CategoriaForm
    success_url = reverse_lazy("producto:lista")