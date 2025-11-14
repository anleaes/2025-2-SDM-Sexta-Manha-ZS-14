from django.db import models

# Create your models here.
class chamado(models.Model):
    titulo = models.CharField('Titulo', max_length=100)
    descricao = models.TextField('Descricao')
    status = models.CharField('Status', choices=[('aberto', 'Aberto'), ('em_andamento', 'Em Andamento'), ('fechado', 'Fechado')], max_length=15)
    dataAbertura = models.DateField('Data Abertura', auto_now_add=True)
    dataFechamento = models.DateField('Data Fechamento', null=True, blank=True) 
    prioridade = models.CharField('Prioridade', choices=[('baixa', 'Baixa'), ('media', 'Média'), ('alta', 'Alta')], max_length=10)
    ans = models.ForeignKey('ans.Ans', on_delete=models.CASCADE, verbose_name='ANS')
  # Create your models here.
     class Meta:
        verbose_name = 'Chamado'
        verbose_name_plural = 'Chamado'
        ordering =['id']

    def __str__(self):
        return f"self.titulo - self.status"