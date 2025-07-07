from django.shortcuts import render
from django.http import JsonResponse
from students.models import *
from employees.models import Employee as EmployeeModel
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.http import Http404



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






@api_view(['GET'])
def fathersView(request):

    if request.method == 'GET':
        # We will get all the data from students table


        father = Father.objects.all()
        serializer = FatherSerializer(father, many =True)

        return Response(serializer.data, status=status.HTTP_200_OK)





@api_view(['GET', 'PUT', 'DELETE'])
def particularstudentView(request, pk):
    # if request.method == 'GET':
    #     partic = Student.objects.get(pk = pk)
    #     print(partic)
    #     if partic != "":
    #         serializer = StudentSerializer(partic)
    #         return Response(serializer.data, status = status.HTTP_302_FOUND)
    #     else:
    #         return Response(serializers.errors, status = status.HTTP_404_NOT_FOUND)
    



    try:
        partic = Student.objects.get(pk=pk)

    except Student.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializ = StudentSerializer(partic)
        return Response (serializ.data, status = status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        serializer = StudentSerializer(partic, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
    
        else:
            return Response(serializers.errors , status = status.HTTP_400_BAD_REQUEST)



    elif request.method == 'DELETE':
        partic.delete()
        return Response(status =  status.HTTP_204_NO_CONTENT)
    









# BELOW WILL BE THE CLASS BASED VIEW FOR THE EMPLOYEE MODEL

class Employee(APIView):
    def get(self, request):
        employees = EmployeeModel.objects.all()
        serializer = EmployeeSerializer(employees, many =True)
        return Response(serializer.data, status = status.HTTP_200_OK)



    def post(self, request):

        serializer = EmployeeSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

class ParticularEmployeeDetail(APIView):

    # we need to get object from database


    def get_object(self,pk):
        try:
            return EmployeeModel.objects.get(pk = pk)
    

        except EmployeeModel.DoesNotExist:
            raise Http404


    def get(self, request, pk):
        employees = self.get_object(pk = pk)
        serializer = EmployeeSerializer(employees)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    def put(self, request, pk):
        employee = self.get_object(pk)

        serializer = EmployeeSerializer(employee, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        
        return Response(serializers.errors, status = status.HTTP_400_BAD_REQUEST)
    


    def delete(self, request, pk):
        data = self.get_object(pk = pk)
        data.delete()
        return Response(status=status.HTTP_404_NOT_FOUND)


