
from rest_framework import viewsets

from .models import Autor
from .serializers import AutorModelSerializer

class AutorModelViewSet(viewsets.ModelViewSet):
    u"""docstring for AutorViewSet"""
    queryset = Autor.objects.all()
    serializer_class = AutorModelSerializer