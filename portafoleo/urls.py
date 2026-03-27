from django.urls import path
from .views import index, categoria_detalle

app_name = 'portafoleo'

urlpatterns = [
    path('', index, name='index'),
    path('categoria/<slug:slug>/', categoria_detalle, name='categoria_detalle'),
]
