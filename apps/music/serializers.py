from rest_framework import serializers
from .models import Autor

class AutorModelSerializer(serializers.ModelSerializer):
    u"""docstring for AutorModelSerializer"""
    
    class Meta:
        model = Autor
        fields = '__all__'
