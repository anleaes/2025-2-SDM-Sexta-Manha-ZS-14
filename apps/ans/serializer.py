
from .models import Ans
from rest_framework import serializers

class AnsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ans
        fields = '__all__'
        
        # Para chamar todos os atributos:
        # fields = '__all__'
        
        # Para chamar somentes os atributos de interesse:
        # fields = ['id','created_on', 'updated_on', 'name', 'description']