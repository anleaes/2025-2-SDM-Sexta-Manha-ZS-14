from django.db import models

# Create your models here.
class Atendimento(models.Model):
    name = models.CharField('Nome', max_length=50)
    description = models.TextField('Descricao', max_length=100)