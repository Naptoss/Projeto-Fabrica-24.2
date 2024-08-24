from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=255)
    rgm = models.CharField(max_length=20, unique=True)
    periodo = models.CharField(max_length=10, choices=[('Matutino', 'Matutino'), ('Vespertino', 'Vespertino'), ('Noturno', 'Noturno')])
    curso = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
