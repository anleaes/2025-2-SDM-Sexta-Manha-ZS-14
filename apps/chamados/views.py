from django.shortcuts import render
from .models import Chamado
from rest_framework import viewsets
from .serializer import ChamadoSerializer
# Create your views here.

class ChamadoViewSet(viewsets.ModelViewSet):
    queryset = Chamado.objects.all()
    serializer_class = ChamadoSerializer  