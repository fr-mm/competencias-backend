from __future__ import annotations

from django.db import models

from aplicacao.models.modelo_unidade_senai import ModeloUnidadeSenai


class ModeloDocente(models.Model):
    nome = models.CharField(max_length=200)
    id = models.UUIDField(primary_key=True, unique=True)
    email = models.EmailField()
    tipo_de_contratacao = models.CharField(max_length=200)
    unidade_senai = models.ForeignKey(ModeloUnidadeSenai, on_delete=models.CASCADE)
    ativo = models.BooleanField()
