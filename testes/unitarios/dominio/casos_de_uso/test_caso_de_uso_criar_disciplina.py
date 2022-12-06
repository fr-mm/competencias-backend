from unittest import TestCase

from mockito import mock, when, verify, unstub

from dominio.casos_de_uso import CasoDeUsoCriarDisciplina
from dominio.otds import OTDDisciplinaEmCriacao, OTDDisciplina
from testes.fabricas import FabricaTesteOTDDisciplinaEmCriacao


class TestCasoDeUsoCriarDisciplina(TestCase):
    def setUp(self) -> None:
        self.disciplina = mock()
        self.repositorio_disciplina = mock()
        self.caso_de_uso = CasoDeUsoCriarDisciplina(
            repositorio_disciplina=self.repositorio_disciplina
        )

    def tearDown(self) -> None:
        unstub()

    def test_executar_QUANDO_disciplina_nao_existe_ENTAO_salva_disciplina_no_repositorio(self) -> None:
        otd_entrada = FabricaTesteOTDDisciplinaEmCriacao.build()
        when(OTDDisciplinaEmCriacao).para_entidade().thenReturn(self.disciplina)
        when(self.repositorio_disciplina).salvar(self.disciplina)
        when(OTDDisciplina).de_entidade(self.disciplina)

        self.caso_de_uso.executar(otd_entrada)

        verify(self.repositorio_disciplina).salvar(self.disciplina)

    def test_executar_QUANDO_disciplina_criada_ENTAO_retorna_otd_disciplina(self) -> None:
        otd_entrada = FabricaTesteOTDDisciplinaEmCriacao.build()
        when(OTDDisciplinaEmCriacao).para_entidade().thenReturn(self.disciplina)
        when(self.repositorio_disciplina).salvar(self.disciplina)
        otd_disciplina = mock()
        when(OTDDisciplina).de_entidade(self.disciplina).thenReturn(otd_disciplina)

        resultado = self.caso_de_uso.executar(otd_entrada)

        self.assertEqual(resultado, otd_disciplina)
