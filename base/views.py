from django.shortcuts import render
from django.http import HttpResponse



# Below is for the normal first codes
# def home(request):
#     return HttpResponse('Home PA atsjhgasdgge')


# def rooms(request):
#     return HttpResponse("This is the ROOM")




# BELOW IS FOR THE HTML, TEMPLATES

def home(request):
    return render(request, 'home.html')

def rooms(request):
    return render(request, 'rooms.html')