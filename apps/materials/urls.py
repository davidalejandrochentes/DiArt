from django.urls import path
from . import views

urlpatterns = [
    path("materiales/", views.materials_list, name="materials"),
    path("materiales/<slug:slug>/", views.category_products, name="materials_category"),
    path(
        "materiales/<slug:slug_cat>/<slug:slug_prod>/",
        views.product_detail,
        name="product_detail",
    ),
]
