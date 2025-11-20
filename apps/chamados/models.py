from django.db import models
from prioridades.models import Prioridade
from clientes.models import Cliente
from django.utils import timezone

# Create your models here.
class Chamado(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(max_length=500)
    status = models.BooleanField('Ativo', default=True)
    dataAbertura = models.DateTimeField(default=timezone.now)
    dataFechamento = models.DateTimeField(default=timezone.now, null=True, blank=True)
    prioridades = models.ForeignKey(Prioridade,on_delete=models.CASCADE)
    clientes = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Chamado'
        verbose_name_plural = 'Chamados'
        ordering =['id']

    def __str__(self):
        return f"{self.titulo}" - f"{self.clientes}"
