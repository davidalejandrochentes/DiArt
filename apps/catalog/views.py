from django.shortcuts import render, get_object_or_404
from .models import Category, GalleryImage


def catalog_list(request):
    categories = Category.objects.filter(activo=True)
    return render(request, "catalog.html", {"categories": categories})


def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug, activo=True)
    images = category.images.filter(activo=True)
    return render(
        request, "catalog_detail.html", {"category": category, "images": images}
    )
