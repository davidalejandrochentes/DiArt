from django.urls import path
from .views import index

app_name = 'portafoleo'

urlpatterns = [
    path('', index, name='index'),
]
