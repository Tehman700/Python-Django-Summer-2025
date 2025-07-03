from django.urls import path
from . import views



# URL ROUTING FILES
urlpatterns = [
    path('tehman/', views.home, name = "home"),
    path('room/', views.rooms , name = "room"),
    path('', views.rooms, name = "khali")
]
