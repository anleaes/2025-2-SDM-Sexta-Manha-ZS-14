from django.db import models
from clientes.models import Cliente
from atendimentos.models import Atendimento

# Create your models here.

class Avaliacao(models.Model):
    nota = models.CharField('Nota', max_length=20, choices=[('Excelente', 'Excelente'), ('Bom', 'Bom'), ('Regular', 'Regular'), ('Ruim', 'Ruim'), ('Pessimo', 'Pessimo')])
    comentario = models.TextField('Comentario', max_length=500)
    dataAvaliacao = models.DateField('Data da Avaliacao')
    clientes = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    atendimento = models.OneToOneField(Atendimento, on_delete=models.CASCADE, related_name="avaliacao")
    
    class Meta:
        verbose_name = 'Avaliacao'
        verbose_name_plural = 'Avaliacoes'
        ordering =['id']

    def __str__(self):
        return self.clientes