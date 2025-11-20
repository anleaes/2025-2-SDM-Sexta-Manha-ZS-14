from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Prioridade(models.Model):
    nome = models.CharField('Nome', max_length=50)
    descricao = models.TextField('Descricao', max_length=200)
    tempoMaximoResposta = models.IntegerField('Tempo Maximo de Resposta (em horas)',[MinValueValidator(1)])
    tempoMaximoResolucao = models.IntegerField('Tempo Maximo de Resolucao (em horas)',[MinValueValidator(1)])
    