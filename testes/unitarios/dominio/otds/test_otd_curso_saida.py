from unittest import TestCase

from mockito import unstub, mock, when

from dominio.entidades import Curso
from dominio.otds import OTDCursoSaida, OTDModulo
from testes.fabricas import FabricaTesteCurso


class TestOTDCursoSaida(TestCase):
    def setUp(self) -> None:
        self.modulo_mock = mock()
        self.otd_modulo_mock = mock()
        when(OTDModulo).de_entidade(...).thenReturn(self.otd_modulo_mock)
        when(OTDModulo).para_entidade(...).thenReturn(self.modulo_mock)

    def tearDown(self) -> None:
        unstub()

    def test_de_entidade_QUANDO_entidade_informada_ENTAO_retorna_otd_esperado(self) -> None:
        curso: Curso = FabricaTesteCurso.build()

        otd = OTDCursoSaida.de_entidade(curso)

        otd_esperado = OTDCursoSaida(
            id=curso.id.valor,
            nome=curso.nome.valor,
            modulos=[self.otd_modulo_mock for _ in range(len(curso.modulos))],
            ativo=otd.ativo
        )
        self.assertEqual(otd, otd_esperado)
