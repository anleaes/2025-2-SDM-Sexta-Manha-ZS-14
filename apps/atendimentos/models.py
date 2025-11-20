from django.db import models
from chamados.models import Chamado
from atendentes.models import Atendente
# Create your models here.

class Atendimento(models.Model):
    dataInicio = models.DateField('Data de Início', auto_now_add=True)
    dataFim = models.DateField('Data de Fim', null=True, blank=True)
    observacoes = models.TextField('Observações', max_length=500, blank=True)
    chamados = models.OneToOneField('chamados.Chamado', on_delete=models.CASCADE)
    atendentes = models.ForeignKey(Atendente, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Atendimento'
        verbose_name_plural = 'Atendimentos'
        ordering =['id']

    def __str__(self):
        return f'{self.chamados} - {self.atendentes}'