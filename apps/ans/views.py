from django.shortcuts import render
from rest_framework import viewsets
from .models import Ans
from .serializer import AnsSerializer
# Create your views here.
class AnsViewSet(viewsets.ModelViewSet):
    queryset = Ans.objects.all()
    serializer_class = AnsSerializer  