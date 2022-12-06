from unittest import TestCase

from mockito import mock, unstub, when, verify

from dominio.casos_de_uso import CasoDeUsoEditarDisciplina
from dominio.entidades import Disciplina
from dominio.otds import OTDDisciplina
from testes.fabricas import FabricaTesteOTDDisciplina, FabricaTesteDisciplina


class TestCasoDeUsoEditarDisciplina(TestCase):

    def setUp(self) -> None:
        self.repositorio_disciplina = mock()
        self.caso_de_uso = CasoDeUsoEditarDisciplina(
            repositorio_disciplina=self.repositorio_disciplina
        )

    def tearDown(self) -> None:
        unstub()

    def test_executar_QUANDO_id_existe_ENTAO_salva_disciplina_no_repositorio(self) -> None:
        otd_disciplina: OTDDisciplina = FabricaTesteOTDDisciplina.build()
        disciplina: Disciplina = FabricaTesteDisciplina.build()
        when(OTDDisciplina).para_entidade().thenReturn(disciplina)
        when(self.repositorio_disciplina).salvar(disciplina)

        self.caso_de_uso.executar(otd_disciplina)

        verify(self.repositorio_disciplina).salvar(disciplina)

    def test_executar_QUANDO_sucesso_ENTAO_retorna_otd_disciplina_esperada(self) -> None:
        otd_entrada: OTDDisciplina = FabricaTesteOTDDisciplina.build()
        disciplina: Disciplina = FabricaTesteDisciplina.build()
        when(OTDDisciplina).para_entidade().thenReturn(disciplina)
        when(self.repositorio_disciplina).salvar(disciplina)

        otd_saida = self.caso_de_uso.executar(otd_entrada)

        self.assertEqual(otd_saida, otd_entrada)
