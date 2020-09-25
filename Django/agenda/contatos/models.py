from django.db import models
from django.utils import timezone

# Create your models here.


class Categoria(models.Model):
    # id: INT(automático)
    nome = models.CharField(max_length=255)  # nome: STR * (obrigatório)

    def __str__(self):
        return self.nome


class Contato(models.Model):
    # id: INT(automático)
    nome = models.CharField(max_length=150)  # nome: STR * (obrigatório)
    sobrenome = models.CharField(max_length=255, blank=True)  # sobrenome: STR (opcional)
    telefone = models.CharField(max_length=255)  # telefone: STR * (obrigatório)
    email = models.CharField(max_length=255, blank=True)  # email: STR (opcional)
    data_criacao = models.DateTimeField(default=timezone.now)  # data_criacao: DATETIME (automático)
    descricao = models.TextField(blank=True)  # descricao: texto
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)  # categoria: CATEGORIA (outro model)
    mostrar = models.BooleanField(default=True)
    foto = models.ImageField(blank=True, upload_to='fotos/%Y/%m/%d')

    def __str__(self):
        return self.nome
