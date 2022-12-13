from unittest import TestCase

from mockito import mock, unstub, when, verify

from dominio.casos_de_uso import CasoDeUsoEditarCurso
from dominio.entidades import Curso
from dominio.erros import ErroCursoNaoEncontrado
from dominio.objetos_de_valor import Id
from dominio.otds import OTDCursoSaida, OTDCursoEntrada
from testes.fabricas import FabricaTesteOTDCursoEntrada, FabricaTesteCurso


class TestCasoDeUsoEditarCurso(TestCase):

    def setUp(self) -> None:
        self.repositorio_curso = mock()
        self.caso_de_uso = CasoDeUsoEditarCurso(
            repositorio_curso=self.repositorio_curso
        )

    def tearDown(self) -> None:
        unstub()

    def test_executar_QUANDO_id_existe_ENTAO_salva_curso_no_repositorio(self) -> None:
        otd_curso: OTDCursoEntrada = FabricaTesteOTDCursoEntrada.build()
        curso: Curso = FabricaTesteCurso.build()
        when(OTDCursoEntrada).para_entidade().thenReturn(curso)
        when(self.repositorio_curso).salvar(curso)

        self.caso_de_uso.executar(otd_curso)

        verify(self.repositorio_curso).salvar(curso)

    def test_executar_QUANDO_id_nao_existe_ENTAO_lanca_erro_curso_nao_encontrado(self) -> None:
        otd: OTDCursoEntrada = FabricaTesteOTDCursoEntrada.build()
        when(self.repositorio_curso).trazer_por_id(Id(otd.id)).thenRaise(ErroCursoNaoEncontrado(otd.id))

        with self.assertRaises(ErroCursoNaoEncontrado):
            self.caso_de_uso.executar(otd)

    def test_executar_QUANDO_sucesso_ENTAO_retorna_otd_curso_esperado(self) -> None:
        otd_entrada: OTDCursoEntrada = FabricaTesteOTDCursoEntrada.build()
        curso: Curso = FabricaTesteCurso.build()
        when(OTDCursoEntrada).para_entidade().thenReturn(curso)
        when(self.repositorio_curso).salvar(curso)

        otd_saida = self.caso_de_uso.executar(otd_entrada)

        esperado = OTDCursoSaida.de_entidade(curso)
        self.assertEqual(otd_saida, esperado)
