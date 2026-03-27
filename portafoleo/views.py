from django.shortcuts import render, get_object_or_404
from .models import Portafolio, CategoriaPortafolio, ImagenCategoria


def index(request):
    portafolio = Portafolio.objects.filter(activo=True).first()
    categorias = CategoriaPortafolio.objects.filter(activo=True)

    context = {
        'portafolio': portafolio,
        'categorias': categorias,
    }
    return render(request, 'portafoleo/index.html', context)


def categoria_detalle(request, slug):
    portafolio = Portafolio.objects.filter(activo=True).first()
    categoria = get_object_or_404(CategoriaPortafolio, slug=slug, activo=True)
    imagenes = ImagenCategoria.objects.filter(categoria=categoria, activo=True)

    context = {
        'portafolio': portafolio,
        'categoria': categoria,
        'imagenes': imagenes,
    }
    return render(request, 'portafoleo/categoria_detalle.html', context)
