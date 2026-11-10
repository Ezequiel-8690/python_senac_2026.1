from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['nome']

    def __str__(self):
        return self.nome

class Receita(models.Model):

    titulo = models.CharField(max_length=200)

    ingredientes = models.TextField(
        help_text="informe um ingrediente por linha."
    )

    modo_preparo = models.TextField(
        help_text="Descreva o passo a passo do preparo."
    )

    tempo_preparoo = models.PositiveBigIntegerField(
        help_text="Tempo total de preparo, em minutos."
    )

    data_publicacao = models.DateTimeField(auto_now_add=True)

    publicada = models.BooleanField(default=False)

    categorias = models.ManyToManyField(
        Categoria,
        related_name="receitas",
        blank=True,
    )

    Autor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="receitas",
    )

    class Meta:
        verbose_name = "Receita"
        verbose_name_plural = "Receitas"
        ordering = ["-data_publicacao"]

    def __str__(self):
        return self.titulo