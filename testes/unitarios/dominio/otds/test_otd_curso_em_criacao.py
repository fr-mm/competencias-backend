from unittest import TestCase

from mockito import mock, when, unstub

from dominio.objetos_de_valor import NomeDeDisciplina
from dominio.otds import OTDCursoEmCriacao, OTDModuloEmCriacao
from testes.fabricas import FabricaTesteOTDCursoEntrada


class TestOTDCursoEmCriacao(TestCase):
    def setUp(self) -> None:
        self.modulo_mock = mock()
        when(OTDModuloEmCriacao).para_entidade(...).thenReturn(self.modulo_mock)

    def tearDown(self) -> None:
        unstub()

    def test_para_entidade_QUANDO_atributos_validos_ENTAO_retorna_docente_com_atributos_esperados(self) -> None:
        otd: OTDCursoEmCriacao = FabricaTesteOTDCursoEntrada.build()

        curso = otd.para_entidade()

        atributos_resultantes = [
            curso.nome,
            curso.modulos,
            curso.ativo
        ]
        atributos_esperados = [
            NomeDeDisciplina(otd.nome),
            [self.modulo_mock for _ in range(len(otd.modulos))],
            otd.ativo
        ]
        self.assertEqual(atributos_resultantes, atributos_esperados)
