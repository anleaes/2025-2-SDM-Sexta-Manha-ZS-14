from django.db import models

# Create your models here.

class ans(models.Model):
    tempoMaximoHoras = models.TimeField('Tempo Maximo')
    dataInicio = models.DateField('Data Inicio')
    dataLimite = models.DateField('Data Limite')
    status = models.CharField('Status', choices=[('ativo', 'Ativo'), ('inativo', 'Inativo')], max_length=10)