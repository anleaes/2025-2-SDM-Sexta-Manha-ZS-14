from django.db import models

# Create your models here.
class Ans(models.Model):
    tempoMaximoHoras = models.IntegerField('Tempo Maximo Horas')
    dataInicio = models.DateField('Data Inicio')
    dataFim = models.DateField('Data Fim')
    status = models.CharField('Status', max_length=50)
    
    class Meta:
        verbose_name = 'Ans'
        verbose_name_plural = 'Ans'
        ordering =['id']

    def __str__(self):
        return f"self.name" - f"self.status"
