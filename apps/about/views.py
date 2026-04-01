from django.shortcuts import render
from .models import About


def about_detail(request):
    about = About.objects.first()
    return render(request, "about.html", {"about": about})
