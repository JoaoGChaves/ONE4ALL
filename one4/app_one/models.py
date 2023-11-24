from django.db import models

class Cadastro(models.Model):
    nomeOrg = models.CharField(max_length=100)
    nomeResp = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=14)
    telefone = models.CharField(max_length=20)
    email = models.EmailField()
    senha = models.CharField(max_length=100)