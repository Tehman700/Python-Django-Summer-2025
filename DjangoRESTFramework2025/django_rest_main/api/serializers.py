from rest_framework import serializers
from students.models import Student,Father



class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = "__all__"





class FatherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Father
        fields = "__all__"