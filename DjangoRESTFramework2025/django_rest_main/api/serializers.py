from rest_framework import serializers
from students.models import Student,Father
from employees.models import Employee



class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = "__all__"





class FatherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Father
        fields = "__all__"



class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = "__all__"