from django.db import models
from django.utils import timezone

# Create your models here.
class Atendimento(models.Model):
    dataInicio = models.DateTimeField(verbose_name='Data de Início',default=timezone.now)
    dataFim = models.DateTimeField(verbose_name='Data de Fim',)
    observacoes = models.TextField(verbose_name='Observações',)
        
    class Meta:
        verbose_name = 'Clientes'
        verbose_name_plural = 'Clientes'
        ordering =['id']

    def __str__(self):
        return f"{self.id}"