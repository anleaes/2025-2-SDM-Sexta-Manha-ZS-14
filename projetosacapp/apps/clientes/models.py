from django.db import models

# Create your models here.
class Clientes(models.Model):
    nome = models.CharField('Nome', max_length=50)
    email = models.EmailField('Email', max_length=100)
    telefone = models.CharField('Telefone', max_length=15)
    endereco = models.CharField('Endereço', max_length=200)