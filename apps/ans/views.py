from django.shortcuts import render
from rest_framework import viewsets
from .models import ans
from .serializer import ansSerializer
# Create your views here.
class ansViewSet(viewsets.ModelViewSet):
    queryset = ans.objects.all()
    serializer_class = ansSerializer  
    