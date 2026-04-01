from django.urls import path
from . import views

urlpatterns = [
    path("catalogo/", views.catalog_list, name="catalog"),
    path("catalogo/<slug:slug>/", views.category_detail, name="category_detail"),
]
