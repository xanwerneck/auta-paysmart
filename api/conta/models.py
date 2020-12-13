from django.db import models
from django.contrib.auth.models import User
from corretora.models import *
from pessoa.models import *

class Conta(models.Model):
    pessoa = models.ForeignKey(to=Pessoa, on_delete=models.CASCADE)
    corretora = models.ForeignKey(to=Corretora, on_delete=models.CASCADE)
    account_id_paysmart = models.CharField(max_length=255, null=True, blank=True)
    psProductCode = models.CharField(max_length=6, null=True, blank=True)
    def __str__(self):
        return self.pessoa.nome

class ContaCorrente(models.Model):
    conta = models.ForeignKey(to=Conta, on_delete=models.CASCADE)
    saldo = models.FloatField()
    def __str__(self):
        return 'Conta ' + self.conta.pessoa.nome

class ContaInvestimento(models.Model):
    conta = models.ForeignKey(to=Conta, on_delete=models.CASCADE)
    
class TipoInvestimento(models.Model):
    descricao = models.CharField(max_length=255)
    def __str__(self):
        return self.descricao

class Investimento(models.Model):
    tipo_investimento = models.ForeignKey(to=TipoInvestimento, on_delete=models.CASCADE)
    valor_investido = models.FloatField()
    conta_investimento = models.ForeignKey(to=ContaInvestimento, on_delete=models.CASCADE)

class CartaoConta(models.Model):
    conta = models.ForeignKey(to=ContaCorrente, on_delete=models.CASCADE)
    pan = models.CharField(max_length=16)
    cvv = models.CharField(max_length=4)
    dateexp = models.CharField(max_length=10)
    cardholder = models.CharField(max_length=150)