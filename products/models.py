from django.db import models

class Product(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.CharField(max_length=255)
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    validade = models.DateField()

    def __str__(self):
        return self.nome