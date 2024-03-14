from django.shortcuts import render
from django.http import HttpResponse
from .models import Cliente, Contacto
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

