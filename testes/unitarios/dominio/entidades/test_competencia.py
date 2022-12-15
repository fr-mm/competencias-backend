from random import randint
from unittest import TestCase

from dominio.entidades import Competencia
from dominio.enums import NivelDeCompetenciaEnum
from dominio.objetos_de_valor import Id
from testes.fabricas import FabricaTesteId


class TestCompetencia(TestCase):
    def test_construir_QUANDO_atributos_informados_ENTAO_retorna_competencia(self) -> None:
        docente_id = FabricaTesteId.build()
        disciplina_id = FabricaTesteId.build()
        nivel = 2

        competencia = Competencia.construir(
            docente_id=docente_id,
            disciplina_id=disciplina_id,
            nivel=nivel
        )

        esperado = Competencia(
            docente_id=Id(docente_id),
            disciplina_id=Id(disciplina_id),
            nivel=NivelDeCompetenciaEnum.DOIS
        )
        self.assertEqual(competencia, esperado)
