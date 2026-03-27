from django.shortcuts import render
from .models import Tienda, CategoriaTienda


def index(request):
    tienda = Tienda.objects.filter(activo=True).first()
    categorias = CategoriaTienda.objects.filter(activo=True)
    
    context = {
        'tienda': tienda,
        'categorias': categorias,
    }
    return render(request, 'tienda/index.html', context)
