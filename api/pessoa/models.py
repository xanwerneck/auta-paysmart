from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Pessoa(models.Model):
    usuario = models.OneToOneField(to=User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=255, null=False, blank=False)
    cpf = models.CharField(max_length=11, null=False, blank=False)
    data_nascimento = models.DateField(null=True, blank=True)
    def __str__(self):
        return self.nome

class TipoEndereco(models.Model):
    descricao = models.CharField(max_length=50)
    def __str__(self):
        return self.descricao

class PessoaEndereco(models.Model):
    pessoa = models.ForeignKey(to=Pessoa, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=500, null=True, blank=True)
    tipo = models.ForeignKey(to=TipoEndereco, on_delete=models.CASCADE, null=True, blank=True)
    numero = models.IntegerField(null=True, blank=True)
    complemento = models.CharField(max_length=150)
    cep = models.CharField(max_length=8, null=True, blank=True)
    def __str__(self):
        return self.pessoa.nome + ' - endereco: ' + self.descricao