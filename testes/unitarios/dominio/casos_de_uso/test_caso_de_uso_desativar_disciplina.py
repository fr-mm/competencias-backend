from unittest import TestCase

from mockito import mock, unstub, when, verify

from dominio.casos_de_uso import CasoDeUsoDesativarDisciplina
from dominio.entidades import Disciplina
from testes.fabricas import FabricaTesteDisciplina


class TestCasoDeUsoDesativarDisciplina(TestCase):

    def setUp(self) -> None:
        self.repositorio_disciplina = mock()
        self.caso_de_uso = CasoDeUsoDesativarDisciplina(
            repositorio_disciplina=self.repositorio_disciplina
        )

    def tearDown(self) -> None:
        unstub()

    def test_executar_QUANDO_chamado_ENTAO_desativa_disciplina(self) -> None:
        disciplina: Disciplina = FabricaTesteDisciplina.build()
        when(self.repositorio_disciplina).trazer_por_id(disciplina.id).thenReturn(disciplina)
        when(disciplina).desativar()

        self.caso_de_uso.executar(disciplina.id.valor)

        verify(disciplina).desativar()

    def test_executar_QUANDO_chamado_ENTAO_salva_disciplina_no_repositorio(self) -> None:
        disciplina: Disciplina = FabricaTesteDisciplina.build()
        when(self.repositorio_disciplina).trazer_por_id(disciplina.id).thenReturn(disciplina)
        when(disciplina).desativar()
        when(self.repositorio_disciplina).salvar(disciplina)

        self.caso_de_uso.executar(disciplina.id.valor)

        verify(self.repositorio_disciplina).salvar(disciplina)
