from django.db import models

# Create your models here.

class Materiais(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=30)
    quantidade = models.PositiveIntegerField()
    descricao = models.CharField(max_length=180)