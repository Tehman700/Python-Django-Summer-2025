from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import mixins, generics
from .serializers import *

# Create your views here.

@api_view(['POST'])
def Mainview(request):
    serializer = CodeExecutionSerializer(data = request.data)
    
    if serializer.is_valid():
        language = serializer.validated_data['language']
        code = serializer.validated_data['code']
        user_input = serializer.validated_data['input']



        if language == "python":
            
        
        result = "Tehman this is the reuslt"

        return Response(result, status=status.HTTP_200_OK)
    return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
