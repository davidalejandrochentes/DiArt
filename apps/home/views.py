from django.shortcuts import render
from .models import Header
from apps.about.models import About


def home(request):
    header = Header.objects.first()
    about = About.objects.first()
    return render(request, "home.html", {"header": header, "about": about})
