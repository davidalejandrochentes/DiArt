from django.shortcuts import render
from .models import TeamMember


def team(request):
    team_members = TeamMember.objects.filter(activo=True)
    return render(request, 'team.html', {'team_members': team_members})
