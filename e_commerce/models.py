from decimal import Decimal

from django.db import models
from django.core.validators import MinValueValidator


class Categoria(models.Model):
    nome = models.CharField(null=False, blank=False, max_length=100)
    descricao = models.TextField(max_length=500, blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome


class Produto(models.Model):
    nome = models.CharField(null=False, blank=False, max_length=255)
    descricao = models.TextField(max_length=1000, blank=True)
    preco = models.DecimalField(null=False, blank=False, validators=[MinValueValidator(Decimal("0.01"))], decimal_places=2, max_digits=10)
    quantidade_estoque = models.PositiveIntegerField(null=False, blank=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=False, blank=False)
    imagem = models.URLField(blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome
