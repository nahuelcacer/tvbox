from django.urls import path, re_path
from . import views

app_name = 'planes'

urlpatterns = [
    path('agregar/', views.agregarPlanes, name="addPlan"),
    path('listar/', views.listarPlanes, name="listPlan"),
    path('listarPlanesPorServicio/', views.listaDePlanesPorServicio, name="listarPlanesPorServicio"),
]