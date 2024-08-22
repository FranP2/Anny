from django.db import models

# Create your models here.
from django.db import models

# País tem um relacionamento de muitos para muitos com Cidade

class Pais(models.Model):
    nome = models.CharField(max_length=100)
    cidades = models.ManyToManyField('Cidade', related_name='paises')

    def _str_(self):
        return self.nome


# Cidade tem um relacionamento de muitos para um com País

class Cidade(models.Model):
    nome = models.CharField(max_length=100)
    populacao = models.PositiveIntegerField()
    pais = models.ForeignKey(Pais, related_name='cidades_rel', on_delete=models.CASCADE)

    def _str_(self):
        return f"{self.nome} (população: {self.populacao})"


# Destino tem um relacionamento de um para um com Cidade

class Destino(models.Model):
    cidade = models.OneToOneField(Cidade, on_delete=models.CASCADE)

    def _str_(self):
        return f"Destino: {self.cidade.nome}"


# Turista sem relacionamento

class Turista(models.Model):
    nome = models.CharField(max_length=100)

    def _str_(self):
        return self.nome