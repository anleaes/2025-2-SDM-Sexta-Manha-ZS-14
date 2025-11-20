from .models import Clientes
from rest_framework import serializers # type: ignore

class ClientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clientes
        fields = '__all__'
        