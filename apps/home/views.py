from django.shortcuts import render
from .models import Header

def home(request):
    header = Header.objects.first()
    return render(request, 'home.html', {'header': header})
