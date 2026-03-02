from django.urls import path
from django.contrib.auth.views import LoginView

from core import views

app_name = "core"

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", LoginView.as_view(template_name="core/login.html"), name="login"),
]
