from django.db import models

# Create your models here.
class Corretora(models.Model):
    nome = models.CharField(max_length=255)
