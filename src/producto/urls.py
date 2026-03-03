from django.urls import path

from producto.views_models import categoria, producto

app_name = "producto"

urlpatterns = [
    # path("lista/", views.categoria_list, name="lista"),
    # path("crear/", views.categoria_create, name="crear"),
    # path("cambiar/<int:pk>", views.categoria_update, name="cambiar"),
    # path("detalle/<int:pk>", views.categoria_detail, name="detalle"),
    # path("borrar/<int:pk>", views.categoria_delete, name="borrar"),
    path("categoria/", categoria.CategoriaList.as_view(), name="lista"),
    path("categoria/crear/", categoria.CategoriaCreate.as_view(), name="crear"),
    path("categoria/detalle/<int:pk>", categoria.CategoriaDetail.as_view(), name="detalle"),
    path("categoria/cambiar/<int:pk>", categoria.CategoriaUpdate.as_view(), name="cambiar"),
    path("categoria/borrar/<int:pk>", categoria.CategoriaDelete.as_view(), name="borrar"),

    # Productos
    path("producto/", producto.ProductoList.as_view(), name="lista_producto"),
    path("producto/crear/", producto.ProductoCreate.as_view(), name="crear_producto"),
    path("producto/detalle/<int:pk>", producto.ProductoDetail.as_view(), name="detalle_producto"),
    path("producto/cambiar/<int:pk>", producto.ProductoUpdate.as_view(), name="cambiar_producto"),
    path("producto/borrar/<int:pk>", producto.ProductoDelete.as_view(), name="borrar_producto"),
]
