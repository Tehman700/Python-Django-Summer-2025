from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def students(request):

    students_data = [
        {
            'id' : 1,
            'name' : "Tehman Hassan",
            'batch' : 2023
        }
    ]

    return HttpResponse(students_data)
