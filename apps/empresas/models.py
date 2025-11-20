from django.db import models
from django.core.validators import RegexValidator
from pessoas.models import Pessoa

# Create your models here.

class Empresa(Pessoa):
    cnpj = models.CharField(max_length=18,unique=True,validators=[RegexValidator(regex=r'^\d{2}\.?\d{3}\.?\d{3}/?\d{4}-?\d{2}$',message='CNPJ inválido. Use o formato 00.000.000/0000-00')])
    
    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'
        ordering =['id']

    def __str__(self):
        return self.name   

    