from django.urls import path

from producto import views

app_name = "producto"

urlpatterns = [
    path("lista/", views.categoria_list, name="lista"),
    path("crear/", views.categoria_create, name="crear"),
    path("detalle/<int:pk>", views.categoria_detail, name="detalle"),
    path("borrar/<int:pk>", views.categoria_delete, name="borrar"),
]
