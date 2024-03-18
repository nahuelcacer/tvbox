from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Cliente, Contacto, Direccion
from apps.suscripciones.models import Suscripcion
from django.db.models import Q
# Create your views here.


def agregarCliente(request):
    if request.method == 'POST':
        print(request.POST)
        nombre = request.POST.get('nombre')
        dni = request.POST.get('dni')
        celular = request.POST.get('celular')
        email = request.POST.get('email')
        calle = request.POST.get('calle')
        numero = request.POST.get('numero_calle')
        
        clienteAdd = Cliente.objects.create(nombre=nombre,dni=dni)

        contactoAdd = Contacto.objects.create(cliente=clienteAdd, celular=celular, email=email)

        direccionAdd = Direccion.objects.create(
            cliente=clienteAdd,
            nombre_calle=calle, 
            numero_calle=numero,
            )




        print(contactoAdd.email)
        print("Nombre:", nombre)
        print("DNI:", dni)
        print("Celular:", celular)
        print("Email:", email)
        print("Calle:", calle)
        print("Número:", numero)
        print("Número:", contactoAdd)
        context = {
            'message':'Se agrego'
        }
        return render(request, 'clientes/agregarClientes.html' ,context)

    else:
        # Si la solicitud no es POST, puedes renderizar el formulario nuevamente o realizar otras acciones

        return render(request, 'clientes/agregarClientes.html')


def listarCliente(request):
    if request.method == 'POST':
        buscador = request.POST.get('buscador')
        
        listarCliente = Cliente.objects.all()
        

        if buscador is not None and not ' ' in buscador:
            clientes = listarCliente.filter(Q(nombre__icontains=buscador) | Q(dni__icontains=buscador))

            context = {
            'clientes':clientes
            }
            return render(request, 'clientes/listarClientes.html' ,context)
    else:

        listaClientes = Cliente.objects.all()
        context = {
            'clientes':listaClientes
        }
        return render(request, 'clientes/listarClientes.html' ,context)

def detalleCliente(request, cliente_id):
    cliente = None
    contacto_cliente = None
    direccion_cliente = None
    suscripcion_activa = None
    try:
        cliente = Cliente.objects.get(pk=cliente_id)
        contacto_cliente = Contacto.objects.get(cliente_id=cliente_id)
        direccion_cliente = Direccion.objects.get(cliente_id=cliente_id)
        suscripcion_activa = Suscripcion.objects.get(cliente_id=cliente_id)
        print(suscripcion_activa)
    except Cliente.DoesNotExist:
        # raise Http404("El cliente no existe")
        context = {
            'message':'El cliente no existe'
        }
        return render(request, 'clientes/errorCliente.html', context)
    except Contacto.DoesNotExist:
        pass  # No hay contacto asociado, contacto_cliente ya es None
    except Direccion.DoesNotExist:
        pass
    except Suscripcion.DoesNotExist:
        pass 
    
    context = {
        'cliente': cliente,
        'contacto': contacto_cliente,
        'direccion': direccion_cliente,
        'suscripcion': suscripcion_activa,

    }
    return render(request, 'clientes/detalleCliente.html', context)
