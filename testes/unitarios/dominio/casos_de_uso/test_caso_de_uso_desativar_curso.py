from unittest import TestCase

from mockito import mock, unstub, when, verify

from dominio.casos_de_uso import CasoDeUsoDesativarCurso
from dominio.entidades import Curso
from testes.fabricas import FabricaTesteCurso


class TestCasoDeUsoDesativarCurso(TestCase):

    def setUp(self) -> None:
        self.repositorio_curso = mock()
        self.caso_de_uso = CasoDeUsoDesativarCurso(
            repositorio_curso=self.repositorio_curso
        )

    def tearDown(self) -> None:
        unstub()

    def test_executar_QUANDO_chamado_ENTAO_desativa_curso(self) -> None:
        curso: Curso = FabricaTesteCurso.build()
        when(self.repositorio_curso).trazer_por_id(curso.id).thenReturn(curso)
        when(curso).desativar()

        self.caso_de_uso.executar(curso.id.valor)

        verify(curso).desativar()

    def test_executar_QUANDO_chamado_ENTAO_salva_curso_no_repositorio(self) -> None:
        curso: Curso = FabricaTesteCurso.build()
        when(self.repositorio_curso).trazer_por_id(curso.id).thenReturn(curso)
        when(curso).desativar()
        when(self.repositorio_curso).salvar(curso)

        self.caso_de_uso.executar(curso.id.valor)

        verify(self.repositorio_curso).salvar(curso)
