from django.shortcuts import render
from django.http import HttpResponse
from .models import Room



# Below is for the normal first codes
# def home(request):
#     return HttpResponse('Home PA atsjhgasdgge')


# def rooms(request):
#     return HttpResponse("This is the ROOM")




# BELOW IS FOR THE HTML, TEMPLATES

def home(request):
    return render(request, 'home.html')

def rooms(request):
    rooms_var = Room.objects.all()
    return render(request, 'rooms.html', {'i' :rooms_var})