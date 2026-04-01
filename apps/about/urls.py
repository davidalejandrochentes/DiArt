from django.urls import path
from . import views

urlpatterns = [
    path("nosotros/", views.about_detail, name="about"),
]
