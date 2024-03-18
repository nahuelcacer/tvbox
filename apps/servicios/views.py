from django.shortcuts import render, redirect
from .models import Servicio
# Create your views here.
def listarServicios(request):
    if request.method == 'POST':


        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        Servicio.objects.create(
            nombre=nombre,
            descripcion=descripcion
        )

        servicios = Servicio.objects.all()

        context = {
            'servicios': servicios
        }
        return render(request, 'servicios/listarServicios.html', context)

    else:
        servicios = Servicio.objects.all()

        context = {
            'servicios': servicios
        }
        return render(request, 'servicios/listarServicios.html', context)


def borrarServicio(request, servicio_id):
    # servicio = Servicio.objects.delete(servicio_id)
    servicio = Servicio.objects.get(pk=servicio_id)
    servicio.delete()

    print(servicio)
    return redirect('servicios:listarServicios')


