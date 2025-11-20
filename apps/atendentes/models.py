from django.db import models
from departamentos.models import Departamento
from empresas.models import Empresa

# Create your models here.



class Atendente(models.Model):
    nome = models.CharField('Nome', max_length=50)
    email = models.TextField('Email', max_length=100)
    nivelAcesso = models.IntegerField('Nível de Acesso',choices=[(1, 'Administrador'),(2, 'Usuário Padrão'),(3, 'Convidado'),] ,default=3)
    departamentos = models.ForeignKey(Departamento,on_delete=models.CASCADE)
    empresas = models.ManyToManyField(Empresa, verbose_name="Empresas") 

    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'
        ordering =['id']

    def __str__(self):
        return f'{self.nome} - {self.nivelAcesso} - {self.departamentos}'
    