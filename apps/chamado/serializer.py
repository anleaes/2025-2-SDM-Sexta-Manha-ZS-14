from .models import chamado
from rest_framework import serializers

class ChamadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = chamado
        fields = '__all__'
        
        # Para chamar todos os atributos:
        # fields = '__all__'
        
        # Para chamar somentes os atributos de interesse:
        # fields = ['id','created_on', 'updated_on', 'name', 'description']