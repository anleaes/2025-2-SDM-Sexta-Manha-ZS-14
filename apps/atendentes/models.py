from django.db import models
from departamentos.models import Departamento
# Create your models here.
NIVEIS_ACESSO = [(1, 'Administrador'),(2, 'Usuário Padrão'),(3, 'Convidado'),]

class Category(models.Model):
    nome = models.CharField('Nome', max_length=50)
    email = models.TextField('Email', max_length=100)
    nivelAcesso = models.IntegerField('Nível de Acesso',choices=NIVEIS_ACESSO,default=3)
    departamentos = models.ManyToManyField(Departamento, blank=False)

    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'
        ordering =['id']

    def __str__(self):
        return f'{self.nome} - {self.get_nivelAcesso_display()} - {self.departamentos.count()}'
    