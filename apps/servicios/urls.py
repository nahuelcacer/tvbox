from django.urls import path, re_path
from . import views

app_name = 'servicios'

urlpatterns = [
    path('', views.listarServicios, name="listarServicios"),
]