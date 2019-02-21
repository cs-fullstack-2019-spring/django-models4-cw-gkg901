from django.http import HttpResponse
from django.shortcuts import render
from .models import State, Citizen



# Create your views here.
def index(request):
    return HttpResponse('index')


def citizens(request):
    places = State.objects.all()
    for where in places:
        print(f'{where.state_name}')
        for info in Citizen.objects.filter(citizen_state__state_name=where.state_name):
            print(info.citizen_first_name)

    return HttpResponse('citizens')


def chgstate(request):
    folks = Citizen.objects.all()
    for last in folks:
        location = Citizen.objects.all()
        # location[2]
        location[2].state_name = "Mississippi"
        print(citizens(request))




