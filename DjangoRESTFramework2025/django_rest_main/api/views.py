from django.shortcuts import render
from django.http import JsonResponse
from students.models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view




# Create your views here.


# def studentsView(request):

#     # Now we will query into the database
#     # Now we wull use manually serialize
#     students_data = Student.objects.all()

#     final = list(students_data.values())

#     return JsonResponse(final, safe= False)




@api_view(['GET', 'POST'])
def studentsView(request):

    if request.method == 'GET':
        # We will get all the data from students table


        students = Student.objects.all()
        serializer = StudentSerializer(students, many =True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    

    elif request.method == 'POST':
        serializer = StudentSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

