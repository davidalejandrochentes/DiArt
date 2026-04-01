from django.shortcuts import render
from .models import Service


def services_list(request):
    services = Service.objects.filter(activo=True)
    return render(request, "services.html", {"services": services})
