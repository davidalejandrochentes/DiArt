from django.urls import path
from . import views

urlpatterns = [
    path('equipo/', views.team, name='team'),
]
