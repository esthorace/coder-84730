from django.urls import path

from producto import views

app_name = "producto"

urlpatterns = [
    # path("lista/", views.categoria_list, name="lista"),
    # path("crear/", views.categoria_create, name="crear"),
    # path("cambiar/<int:pk>", views.categoria_update, name="cambiar"),
    # path("detalle/<int:pk>", views.categoria_detail, name="detalle"),
    # path("borrar/<int:pk>", views.categoria_delete, name="borrar"),
    path("cambiar/<int:pk>", views.CategoriaUpdate.as_view(), name="cambiar"),
    path("lista/", views.CategoriaList.as_view(), name="lista"),
    path("crear/", views.CategoriaCreate.as_view(), name="crear"),
    path("detalle/<int:pk>", views.CategoriaDetail.as_view(), name="detalle"),
    path("borrar/<int:pk>", views.CategoriaDelete.as_view(), name="borrar"),
]
