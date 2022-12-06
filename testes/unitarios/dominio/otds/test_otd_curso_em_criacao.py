from unittest import TestCase

from dominio.objetos_de_valor import Id, NomeDeDisciplina
from dominio.otds import OTDCursoEmCriacao
from testes.fabricas import FabricaTesteOTDCurso


class TestOTDCurso(TestCase):
    def test_para_entidade_QUANDO_atributos_validos_ENTAO_retorna_docente_com_atributos_esperados(self) -> None:
        otd: OTDCursoEmCriacao = FabricaTesteOTDCurso.build()

        curso = otd.para_entidade()

        atributos_resultantes = [
            curso.nome,
            curso.modulos_ids,
            curso.ativo
        ]
        atributos_esperados = [
            NomeDeDisciplina(otd.nome),
            [Id(id_) for id_ in otd.modulos_ids],
            otd.ativo
        ]
        self.assertEqual(atributos_resultantes, atributos_esperados)
