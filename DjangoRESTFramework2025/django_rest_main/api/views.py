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
from rest_framework import mixins, generics
from blogs.models import *
from blogs.serializers import *



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

# class Employee(APIView):
#     def get(self, request):
#         employees = EmployeeModel.objects.all()
#         serializer = EmployeeSerializer(employees, many =True)
#         return Response(serializer.data, status = status.HTTP_200_OK)



#     def post(self, request):

#         serializer = EmployeeSerializer(data = request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
        
#         return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

# class ParticularEmployeeDetail(APIView):

#     # we need to get object from database


#     def get_object(self,pk):
#         try:
#             return EmployeeModel.objects.get(pk = pk)
    

#         except EmployeeModel.DoesNotExist:
#             raise Http404


#     def get(self, request, pk):
#         employees = self.get_object(pk = pk)
#         serializer = EmployeeSerializer(employees)
#         return Response(serializer.data, status = status.HTTP_200_OK)
    
#     def put(self, request, pk):
#         employee = self.get_object(pk)

#         serializer = EmployeeSerializer(employee, data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status = status.HTTP_200_OK)
        
#         return Response(serializers.errors, status = status.HTTP_400_BAD_REQUEST)
    


#     def delete(self, request, pk):
#         data = self.get_object(pk = pk)
#         data.delete()
#         return Response(status=status.HTTP_404_NOT_FOUND)














"""""
# BELOW IS THE METHOD FOR MIXINS IN CLASS BASED VIEWS

class Employee(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):

    queryset = EmployeeModel.objects.all()
    serializer_class = EmployeeSerializer

    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)
    

# Primary Key Based Operations
class ParticularEmployeeDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = EmployeeModel.objects.all()
    serializer_class = EmployeeSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk)
    
    def put(self, request, pk):
        return self.update(request ,pk)
    
    def delete(self, request, pk):
        return self.destroy(request,pk)
    
"""""




# Now we are using Generics for most short code
""""
    Generics are like this:
    ListAPIView    -  for listing the objects
    CreateAPIView  -  for creating the objects
    RetrieveAPIView - for retrieving a single object using pk
    UpdateAPIView  -  for updating a single object using pk
    DestroyAPIView -  for deleting an object using pk

    COMBINATION ALSO WORKS:

    ListCreateAPIView  - For listing and creating objects
    RetrieveUpdateAPIView  -  For retreiving and updating objects using pk
    RetrieveUpdateDestroyAPIView  - For listing, Updating and Destroying any object using pk

    
"""







class Employee(generics.ListCreateAPIView):
    queryset = EmployeeModel.objects.all()
    serializer_class = EmployeeSerializer


class ParticularEmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = EmployeeModel.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'pk'







class BlogsView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class CommentsView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer



class BlogDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field = 'pk'

class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = 'pk'


    

