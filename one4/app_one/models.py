from django.db import models
from django import forms


class Cadastro(models.Model):
    nomeOrg = models.CharField(max_length=100, null=False)
    nomeResp = models.CharField(max_length=100, null=False)
    cnpj = models.CharField(max_length=14, null=False)
    telefone = models.CharField(max_length=11, null=False)
    email = models.EmailField(null=False)
    senha = models.CharField(max_length=100, null=False)
    def save(self, *args, **kwargs):
        print("Método save chamado")
        super().save(*args, **kwargs)
