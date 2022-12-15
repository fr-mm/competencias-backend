from typing import List

from django.test import TestCase

from aplicacao.models import ModeloCompetencia, ModeloDisciplina, ModeloDocente
from dominio.entidades import Competencia
from dominio.enums import NivelDeCompetenciaEnum
from dominio.objetos_de_valor import Id
from testes.fabricas import FabricaTesteCompetencia, FabricaTesteModeloDisciplina, FabricaTesteModeloDocente, \
    FabricaTesteModeloCompetencia


class TestModeloCompetencia(TestCase):
    def test_para_entidade_QUANDO_entidade_informada_ENTAO_retorna_modelo(self) -> None:
        disciplina: ModeloDisciplina = FabricaTesteModeloDisciplina.create()
        docente: ModeloDocente = FabricaTesteModeloDocente.create()
        competencia: Competencia = FabricaTesteCompetencia.build(
            docente_id=Id(docente.id),
            disciplina_id=Id(disciplina.id)
        )

        modelo = ModeloCompetencia.de_entidade(competencia)

        resultado = {
            'docente': modelo.docente.id,
            'disciplina': modelo.disciplina.id,
            'nivel': modelo.nivel
        }
        esperado = {
            'docente': docente.id,
            'disciplina': disciplina.id,
            'nivel': competencia.nivel.value
        }
        self.assertEqual(resultado, esperado)

    def test_de_entidadade_QUANDO_chamado_ENTAO_retorna_entidade_esperada(self) -> None:
        modelo: ModeloCompetencia = FabricaTesteModeloCompetencia.build()

        competencia = modelo.para_entidade()

        esperado = Competencia(
            disciplina_id=Id(modelo.disciplina.id),
            docente_id=Id(modelo.docente.id),
            nivel=NivelDeCompetenciaEnum(modelo.nivel)
        )
        self.assertEqual(competencia, esperado)
