from django.urls import path, re_path
from . import views


urlpatterns = {
    path('agregar/', views.agregarCliente, name="addCliente"),
    path('listar/', views.listarCliente, name="listCliente")
}