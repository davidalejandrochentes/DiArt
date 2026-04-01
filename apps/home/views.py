from django.shortcuts import render
from .models import Header
from apps.about.models import About
from apps.services.models import Service


def home(request):
    header = Header.objects.first()
    about = About.objects.first()
    services = Service.objects.filter(activo=True)[:3]
    return render(
        request, "home.html", {"header": header, "about": about, "services": services}
    )
