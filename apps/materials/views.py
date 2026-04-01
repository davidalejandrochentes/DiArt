from django.shortcuts import render, get_object_or_404
from .models import MaterialCategory, Product


def materials_list(request):
    categories = MaterialCategory.objects.filter(activo=True)
    return render(request, "materials.html", {"categories": categories})


def category_products(request, slug):
    category = get_object_or_404(MaterialCategory, slug=slug, activo=True)
    products = category.productos.filter(activo=True)
    return render(
        request, "materials_category.html", {"category": category, "products": products}
    )


def product_detail(request, slug_cat, slug_prod):
    category = get_object_or_404(MaterialCategory, slug=slug_cat, activo=True)
    product = get_object_or_404(
        Product, slug=slug_prod, categoria=category, activo=True
    )
    return render(
        request, "product_detail.html", {"category": category, "product": product}
    )
