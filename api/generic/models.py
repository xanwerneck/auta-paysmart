from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Integradora(models.Model):
    api_key = models.CharField(max_length=255)
    status = models.BooleanField(default=True, null=True, blank=True)
    descricao = models.CharField(max_length=255)
    user = models.OneToOneField(to=User, blank=True, null=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.descricao