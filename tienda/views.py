from django.shortcuts import render, get_object_or_404
from .models import Tienda, CategoriaTienda, Producto


def index(request):
    tienda = Tienda.objects.filter(activo=True).first()
    categorias = CategoriaTienda.objects.filter(activo=True)

    context = {
        'tienda': tienda,
        'categorias': categorias,
    }
    return render(request, 'tienda/index.html', context)


def categoria_detalle(request, slug):
    tienda = Tienda.objects.filter(activo=True).first()
    categoria = get_object_or_404(CategoriaTienda, slug=slug, activo=True)
    productos = Producto.objects.filter(categoria=categoria, activo=True)

    context = {
        'tienda': tienda,
        'categoria': categoria,
        'productos': productos,
    }
    return render(request, 'tienda/categoria_detalle.html', context)
