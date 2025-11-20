from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

class Departamento(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    descricao = models.TextField(blank=True, null=True)
    telefoneContato = models.CharField(
    max_length=15,
    blank=True,
    validators=[
        RegexValidator(
            regex=r'^\(?\d{2}\)?\s?\d{4,5}-?\d{4}$',
            message='Informe um telefone válido, ex: (51) 99999-8888.'
        )
    ]
)
    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'
        ordering =['id']

    def __str__(self):
        return f'{self.nome} - {self.telefoneContato}'