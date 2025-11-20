from django.db import models
from pessoas.models import Pessoa

# Create your models here.

class Cliente(Pessoa):
    cpf = models.CharField('CPF', max_length=14, unique=True)
    
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering =['id']

    def __str__(self):
        return self.nome  