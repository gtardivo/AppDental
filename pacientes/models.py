from django.db import models


class Pacientes(models.Model):
    nome = models.CharField(max_length=20)
    cpf = models.CharField(max_length=20)
    endereco = models.CharField(max_length=20)
    cel = models.CharField(max_length=20)

    def __str__(self):
        return self.nome
