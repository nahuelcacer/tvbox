from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render
from apps.suscripciones.models import Suscripcion
def sendEmail(request):

    # send_mail(
    #     'Asunto del correo electrónico',
    #     'Cuerpo del correo electrónico.',
    #     'nahuelcaceres@escribanoschaco.com',  # Dirección de correo electrónico del remitente
    #     ['nahuelcaceres@escribanoschaco.com', 'nahuecaceres29@gmail.com'],  # Lista de direcciones de correo electrónico de los destinatarios
    #     fail_silently=False,
    # )
    html = "<html><body>It is now.</body></html>" 
    return HttpResponse(html)
    # 

def index(request):
    sus = Suscripcion.objects.all()
    context = {
        'sus':sus
    }
    
    return render(request, 'home.html', context)

