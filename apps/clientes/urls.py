from django.urls import path, re_path
from . import views

app_name = 'clientes'

urlpatterns = [
    path('agregar/', views.agregarCliente, name="addCliente"),
    path('listar/', views.listarCliente, name="listCliente"),
    path('<int:cliente_id>/', views.detalleCliente, name="detailCliente")
]