from django.db import models


class dados(models.Model):
    rua = models.CharField(max_length=200)
    localidade = models.CharField(max_length=200)
    bairro = models.CharField(max_length=200)