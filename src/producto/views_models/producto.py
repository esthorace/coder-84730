from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from .. import models
from .. import forms


class ProductoList(ListView):
	model = models.Producto

	def get_queryset(self):
		consulta = self.request.GET.get("consulta")
		if consulta:
			productos = models.Producto.objects.filter(
				Q(nombre__icontains=consulta) | Q(descripcion__icontains=consulta)
			)
		else:
			productos = models.Producto.objects.all()
		return productos


class ProductoDetail(DetailView):
	model = models.Producto


class ProductoDelete(DeleteView):
	model = models.Producto
	success_url = reverse_lazy("producto:lista_producto")


class ProductoCreate(CreateView):
	model = models.Producto
	form_class = forms.ProductoForm
	success_url = reverse_lazy("producto:lista_producto")


class ProductoUpdate(UpdateView):
	model = models.Producto
	form_class = forms.ProductoForm
	success_url = reverse_lazy("producto:lista_producto")

