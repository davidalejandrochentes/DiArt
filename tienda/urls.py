from django.urls import path
from .views import index

app_name = 'tienda'

urlpatterns = [
    path('', index, name='index'),
]
