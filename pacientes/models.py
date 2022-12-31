from django.db import models


class Pacientes(models.Model):
    nome = models.CharField(max_length=100)
    senha = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    cpf = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    cel = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
