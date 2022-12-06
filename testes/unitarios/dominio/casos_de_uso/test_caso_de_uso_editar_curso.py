from unittest import TestCase

from mockito import mock, unstub, when, verify

from dominio.casos_de_uso import CasoDeUsoEditarCurso
from dominio.entidades import Curso
from dominio.otds import OTDCurso
from testes.fabricas import FabricaTesteOTDCurso, FabricaTesteCurso


class TestCasoDeUsoEditarCurso(TestCase):

    def setUp(self) -> None:
        self.repositorio_curso = mock()
        self.caso_de_uso = CasoDeUsoEditarCurso(
            repositorio_curso=self.repositorio_curso
        )

    def tearDown(self) -> None:
        unstub()

    def test_executar_QUANDO_id_existe_ENTAO_salva_curso_no_repositorio(self) -> None:
        otd_curso: OTDCurso = FabricaTesteOTDCurso.build()
        curso: Curso = FabricaTesteCurso.build()
        when(OTDCurso).para_entidade().thenReturn(curso)
        when(self.repositorio_curso).salvar(curso)

        self.caso_de_uso.executar(otd_curso)

        verify(self.repositorio_curso).salvar(curso)

    def test_executar_QUANDO_sucesso_ENTAO_retorna_otd_curso_esperado(self) -> None:
        otd_entrada: OTDCurso = FabricaTesteOTDCurso.build()
        curso: Curso = FabricaTesteCurso.build()
        when(OTDCurso).para_entidade().thenReturn(curso)
        when(self.repositorio_curso).salvar(curso)

        otd_saida = self.caso_de_uso.executar(otd_entrada)
        print(otd_saida)
        print(otd_entrada)
        self.assertEqual(otd_saida, otd_entrada)
