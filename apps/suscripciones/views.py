from django.shortcuts import render, redirect
from apps.clientes.models import Cliente
from apps.planes.models import Plan
from .models import Suscripcion
from datetime import datetime, timedelta

# Create your views here.


def agregarSuscripcion(request, cliente_id):
    if request.method == 'POST':
        comienzo_suscripcion = request.POST.get('comienzo_suscripcion')
        plan = request.POST.get('plan')
        equipo = request.POST.get('equipo')




        cliente_seleccionado = Cliente.objects.get(pk=cliente_id)
        plan_seleccionado = Plan.objects.get(pk=plan)

        # print(plan_seleccionado)

        fecha_comienzo_obj = datetime.strptime(comienzo_suscripcion, "%Y-%m-%d")

        fecha_final_obj = fecha_comienzo_obj + timedelta(days=30)


        Suscripcion.objects.create(
            plan=plan_seleccionado,
            cliente=cliente_seleccionado,
            equipo=equipo,
            comienzo_suscripcion = fecha_comienzo_obj,
            fin_suscripcion = fecha_final_obj
        )

        return redirect('clientes:detailCliente', cliente_id=cliente_id)
    else:
        cliente = Cliente.objects.get(pk=cliente_id)
        planes = Plan.objects.all()

        context = {
            'cliente':cliente,
            'planes':planes,
        }
        return render(request, 'suscripciones/agregarSuscripcion.html', context)