from django.shortcuts import render
from .models import Header
from apps.about.models import About
from apps.services.models import Service
from apps.catalog.models import Category
from apps.team.models import TeamMember


def home(request):
    header = Header.objects.first()
    about = About.objects.first()
    services = Service.objects.filter(activo=True)[:3]
    categories = Category.objects.filter(activo=True, destacado=True)[:3]
    team_members = TeamMember.objects.filter(activo=True)
    return render(
        request,
        "home.html",
        {
            "header": header,
            "about": about,
            "services": services,
            "categories": categories,
            "team_members": team_members,
        },
    )
