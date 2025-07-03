from django.contrib import admin
from django.urls import path
from django.http import HttpResponse




def home(request):
    return HttpResponse('Home PA atsjhgasdgge')


def rooms(request):
    return HttpResponse("This is the ROOM")


# URL ROUTING FILES
urlpatterns = [
    path('admin/', admin.site.urls),
    path('tehman/', home),
    path('room/', rooms)
]
