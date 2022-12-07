from django.db import models

from aplicacao.models.modelo_modulo import ModeloModulo
from aplicacao.models.modelo_disciplina import ModeloDisciplina


class ModeloDisciplinaEmModulo(models.Model):
    modulo = models.ForeignKey(ModeloModulo, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(ModeloDisciplina, on_delete=models.CASCADE)
