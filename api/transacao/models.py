from django.db import models

from conta.models import *

# Create your models here.
class TipoTransacao(models.Model):
    descricao = models.CharField(max_length=150)
    credito_debito = models.IntegerField()

class Transacao(models.Model):
    conta = models.ForeignKey(to=ContaCorrente, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)
    obs = models.CharField(max_length=255)
    authorization_id = models.CharField(max_length=50, null=True, blank=True)
