from .models import Prioridade
from rest_framework import serializers

class PrioridadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prioridade
        fields = '__all__'