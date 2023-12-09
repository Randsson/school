from django.db import models

class Student(models.Model):
    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=14, unique=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.nome} {self.sobrenome}"