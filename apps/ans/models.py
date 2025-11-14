from django.db import models

# Create your models here.

class Ans(models.Model):
    tempoMaximoHoras = models.TimeField('Tempo Maximo')
    dataInicio = models.DateField('Data Inicio')
    dataLimite = models.DateField('Data Limite')
    status = models.CharField('Status', choices=[('ativo', 'Ativo'), ('inativo', 'Inativo')], max_length=10)

    class Meta:
        verbose_name = 'ans'
        verbose_name_plural = 'ans'
        ordering =['id']

    def __str__(self):
        return f"self.dateInicio - self.dataLimite",