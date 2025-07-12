from rest_framework import serializers



class CodeExecutionSerializer(serializers.Serializer):
    
    language = serializers.CharField(max_length = 100)
    code = serializers.CharField()
    input = serializers.CharField(required=False, allow_blank=True)