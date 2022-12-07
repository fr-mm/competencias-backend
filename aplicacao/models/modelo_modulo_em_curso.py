from django.db import models

from aplicacao.models.modelo_modulo import ModeloModulo
from aplicacao.models.modelo_curso import ModeloCurso


class ModeloModuloEmCurso(models.Model):
    modulo = models.ForeignKey(ModeloModulo, on_delete=models.CASCADE)
    curso = models.ForeignKey(ModeloCurso, on_delete=models.CASCADE)
