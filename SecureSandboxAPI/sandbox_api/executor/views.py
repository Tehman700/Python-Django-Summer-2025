from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import mixins, generics
from .serializers import *


import sys
import io
import contextlib

# Create your views here.

@api_view(['POST'])
def Mainview(request):
    serializer = CodeExecutionSerializer(data = request.data)
    
    if serializer.is_valid():
        language = serializer.validated_data['language']
        code = serializer.validated_data['code']
        user_input = serializer.validated_data['input']
        code = f"""{code}"""



        if language == "python":
            @contextlib.contextmanager
            def capture_stdout():
                old_stdout = sys.stdout
                sys.stdout = io.StringIO()
                try:
                    yield sys.stdout
                finally:
                    sys.stdout = old_stdout

        





            def run_code_with_input(code: str, fake_input: str):
                global result
                input_values = fake_input.split('\n')
                input_index = 0

                def mock_input(prompt=''):
                    nonlocal input_index
                    if input_index < len(input_values):
                        val = input_values[input_index]
                        input_index += 1
                        return val
                    return ''

                with capture_stdout() as stdout:
                    # Backup original input and patch it
                    original_input = __builtins__.__dict__.get('input')
                    __builtins__.__dict__['input'] = mock_input

                    try:
                        exec(code, {})  # ⚠️ Executes the user code
                    except Exception as e:
                        print(f"Error: {e}")
                    finally:
                        # Restore original input
                        __builtins__.__dict__['input'] = original_input

                result = stdout.getvalue().strip()


        return Response(result)
    return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
