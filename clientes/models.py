# -*-coding: utf-8 -*-
from django.db import models

# definição das classes herdando do Model do Django
class Cliente (models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    senha = models.CharField(max_length=20)
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=15)

    # nome que referencia o objeto
    def __unicode__(self):
        return self.nome

class Cartao (models.Model):
    TIPO_CHOICES = (
        ('V', 'Visa'),
        ('M', 'Master'),
        ('A', 'American Express')
    )
    tipo = models.CharField(max_length=1, choices=TIPO_CHOICES)
    nome = models.CharField(max_length=50)
    numero = models.CharField(max_length=10)
    data_vencimento = models.DateField()
    codigo_seguranca = models.IntegerField()
    cliente = models.ForeignKey('Cliente')

    def __unicode__(self):
        return self.numero

class Prato (models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    ingredientes = models.CharField(max_length=500)
    codigo = models.CharField(max_length=10)

    def __unicode__(self):
        return self.nome

class Pedido (models.Model):
    cliente = models.ForeignKey('Cliente')
    pratos = models.ForeignKey('Prato')
    cartao = models.ForeignKey('Cartao')
    total = models.DecimalField(max_digits=5, decimal_places=2)
    data = models.DateTimeField(auto_now_add=True)
