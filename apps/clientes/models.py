from django.db import models

# Create your models here.

class Cliente(models.Model):
    nome = models.CharField('Nome', max_length=50)
    email = models.EmailField('Email', max_length=50)
    telefone = models.CharField('Telefone', max_length=50)
    endereco = models.CharField('Endereço', max_length=50)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering =['id']

    def __str__(self):
        return self.nome  