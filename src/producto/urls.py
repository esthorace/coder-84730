from django.urls import path

from producto import views

app_name = "producto"

urlpatterns = [
    path("lista/", views.producto_list, name="lista"),
]
