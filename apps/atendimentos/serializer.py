from .models import Atendimento
from rest_framework import serializers

class AtendimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Atendimento
        fields = '__all__'
