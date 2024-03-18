from django.urls import path, re_path
from . import views

app_name = 'suscripciones'

urlpatterns = [
    path('agregar/<int:cliente_id>', views.agregarSuscripcion, name="addSuscripcion")

]