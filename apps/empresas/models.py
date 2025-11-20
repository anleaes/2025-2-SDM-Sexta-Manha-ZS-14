from django.db import models
from django.core.validators import RegexValidator
# Create your models here.

class Empresa(models.Model):
    nome = models.CharField(max_length=255)
    cnpj = models.CharField(
    max_length=18,
    unique=True,
    validators=[
        RegexValidator(
            regex=r'^\d{2}\.?\d{3}\.?\d{3}/?\d{4}-?\d{2}$',
            message='CNPJ inválido. Use o formato 00.000.000/0000-00'
        )
    ]
)
    endereco = models.CharField(max_length=255)
    telefone = models.CharField(
    max_length=15,
    blank=True,
    validators=[
        RegexValidator(
            regex=r'^\(?\d{2}\)?\s?\d{4,5}-?\d{4}$',
            message='Informe um telefone válido, ex: (51) 99999-8888.'
        )
    ]
)
    emailContato = models.EmailField(max_length=30,unique=True)

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'
        ordering =['id']

    def __str__(self):
        return self.name   

    