from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.


def studentsView(request):
    students_data = [
        {
            'id' : 1,
            'name' : "Tehman Hassan",
            'batch' : 2023
        }
    ]

    return JsonResponse(students_data, safe=False)