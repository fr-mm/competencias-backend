from __future__ import annotations

from django.db import models

from aplicacao.models.modelo_docente import ModeloDocente
from dominio.objetos_de_valor import Telefone


class ModeloTelefone(models.Model):
    numero = models.CharField(primary_key=True, max_length=14)
    docente = models.ForeignKey(ModeloDocente, on_delete=models.CASCADE)

    def para_objeto_de_valor(self) -> Telefone:
        return Telefone(str(self.numero))
