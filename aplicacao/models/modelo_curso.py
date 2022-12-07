from django.db import models


class ModeloCurso(models.Model):
    id = models.UUIDField(primary_key=True, unique=True)
    nome = models.CharField(max_length=200)
    ativo = models.BooleanField()
