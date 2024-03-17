from django.shortcuts import render
from apps.servicios.models import Servicio
from .models import Plan
from django.http import JsonResponse
# Create your views here.


def agregarPlanes(request):
    if request.method == 'POST':

        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        servicio = request.POST.get('servicio')
        precio = float(request.POST.get('precio'))


        plan_creado = Plan.objects.create(
            nombre=nombre,
            descripcion=descripcion,
            servicio_id=servicio,
            precio=precio
        )




        
        servicios = Servicio.objects.all()

        context = {
            'servicios': servicios,
            'message': f'Se creo el plan  {plan_creado} con exito',
        }


        return render(request, 'planes/agregarPlanes.html', context )
    else:
        servicios = Servicio.objects.all()

        context = {
            'servicios': servicios
        }

        return render(request, 'planes/agregarPlanes.html', context)

def listarPlanes(request):
    servicios = Servicio.objects.all()

    context = {
        'servicios': servicios
    }


    return render (request, 'planes/listarPlan.html', context)
def listaDePlanesPorServicio(request):
    servicio_id = request.GET.get('servicio_id')

    planes = Plan.objects.filter(servicio_id=servicio_id)

    # Serializar los objetos Plan a un formato JSON
    planes_serializados = [
        {
            'id': plan.id,
            'nombre': plan.nombre,
            'descripcion': plan.descripcion,
            'creado_en': plan.creado_en,  # Convertir a cadena ISO 8601
            'precio': plan.precio
        } 
        for plan in planes
    ]

    # Devolver la respuesta HTTP con los datos serializados
    return JsonResponse(planes_serializados, safe=False)

