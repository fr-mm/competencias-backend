from unittest import TestCase

from mockito import mock, unstub, when, verify

from dominio.casos_de_uso import CasoDeUsoCriarCurso
from dominio.otds import OTDCursoEmCriacao, OTDCurso
from testes.fabricas import FabricaTesteOTDCursoEmCriacao


class TestCasoDeUsoCriarCurso(TestCase):

    def setUp(self) -> None:
        self.curso = mock()
        self.repositorio_curso = mock()
        self.caso_de_uso = CasoDeUsoCriarCurso(
            repositorio_curso=self.repositorio_curso
        )

    def tearDown(self) -> None:
        unstub()

    def test_executar_QUANDO_curso_nao_existe_ENTAO_salva_curso_no_repositorio(self) -> None:
        otd_entrada = FabricaTesteOTDCursoEmCriacao.build()
        when(OTDCursoEmCriacao).para_entidade().thenReturn(self.curso)
        when(self.repositorio_curso).salvar(self.curso)
        when(OTDCurso).de_entidade(self.curso)

        self.caso_de_uso.executar(otd_entrada)

        verify(self.repositorio_curso).salvar(self.curso)

    def test_executar_QUANDO_curso_criada_ENTAO_retorna_otd_curso(self) -> None:
        otd_entrada = FabricaTesteOTDCursoEmCriacao.build()
        when(OTDCursoEmCriacao).para_entidade().thenReturn(self.curso)
        when(self.repositorio_curso).salvar(self.curso)
        otd_curso = mock()
        when(OTDCurso).de_entidade(self.curso).thenReturn(otd_curso)

        resultado = self.caso_de_uso.executar(otd_entrada)

        self.assertEqual(resultado, otd_curso)
