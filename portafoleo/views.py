from django.shortcuts import render
from .models import Portafolio, CategoriaPortafolio


def index(request):
    portafolio = Portafolio.objects.filter(activo=True).first()
    categorias = CategoriaPortafolio.objects.filter(activo=True)
    
    context = {
        'portafolio': portafolio,
        'categorias': categorias,
    }
    return render(request, 'portafoleo/index.html', context)
