from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.

class Prioridade(models.Model):
    nome = models.CharField('Nome', max_length=50)
    descricao = models.TextField('Descricao', max_length=200)
    tempoMaximoResposta = models.IntegerField('Tempo Maximo de Resposta (em horas)',validators=[MinValueValidator(1)])
    tempoMaximoResolucao = models.IntegerField('Tempo Maximo de Resolucao (em horas)',validators=[MinValueValidator(1)])


    class Meta:
        verbose_name = 'Prioridades'
        verbose_name_plural = 'Prioridades'
        ordering =['id']

    def __str__(self):
        return f'{self.nome} - {self.descricao}' 
    
    