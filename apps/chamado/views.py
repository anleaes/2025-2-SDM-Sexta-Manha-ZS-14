from django.shortcuts import render
from rest_framework import viewsets
from .models import chamado
from .serializer import ChamadoSerializer

# Create your views here.
class ChamadoViewSet(viewsets.ModelViewSet):
    queryset = chamado.objects.all()
    serializer_class = ChamadoSerializer  
    