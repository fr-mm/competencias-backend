from unittest import TestCase
from mockito import mock, unstub, when, verify

from dominio.casos_de_uso import CasoDeUsoDesativarDocente
from dominio.entidades import Docente
from testes.fabricas import FabricaTesteDocente


class TestCasoDeUsoDesativarDocente(TestCase):
    def setUp(self) -> None:
        self.repositorio_docente = mock()
        self.caso_de_uso = CasoDeUsoDesativarDocente(
            repositorio_docente=self.repositorio_docente
        )

    def tearDown(self) -> None:
        unstub()

    def test_executar_QUANDO_chamado_ENTAO_desativa_docente(self) -> None:
        docente: Docente = FabricaTesteDocente.build()
        when(self.repositorio_docente).trazer_por_id(docente.id).thenReturn(docente)
        when(docente).desativar()

        self.caso_de_uso.executar(docente.id.valor)

        verify(docente).desativar()

    def test_executar_QUANDO_chamado_ENTAO_salva_docente_no_repositorio(self) -> None:
        docente: Docente = FabricaTesteDocente.build()
        when(self.repositorio_docente).trazer_por_id(docente.id).thenReturn(docente)
        when(docente).desativar()
        when(self.repositorio_docente).salvar(docente)

        self.caso_de_uso.executar(docente.id.valor)

        verify(self.repositorio_docente).salvar(docente)
