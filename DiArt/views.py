from django.shortcuts import render
from tienda.models import Tienda
from portafoleo.models import Portafolio


def home(request):
    tienda = Tienda.objects.filter(activo=True).first()
    portafolio = Portafolio.objects.filter(activo=True).first()
    
    context = {
        'tienda': tienda,
        'portafolio': portafolio,
    }
    return render(request, 'home.html', context)
