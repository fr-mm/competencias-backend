from unittest import TestCase
from mockito import mock, unstub, when, verify

from testes.fabricas import FabricaTesteOTDDocente, FabricaTesteDocente
from dominio.otds import OTDDocente
from dominio.erros import ErroDocenteNaoEncontrado
from dominio.casos_de_uso import CasoDeUsoEditarDocente
from dominio.entidades import Docente


class TestCasoDeUsoEditarDocente(TestCase):
    def setUp(self) -> None:
        self.repositorio_docente = mock({
            'id_existe': lambda id_: None,
            'salvar': lambda docente: None
        })
        self.caso_de_uso = CasoDeUsoEditarDocente(
            repositorio_docente=self.repositorio_docente
        )

    def tearDown(self) -> None:
        unstub()

    def test_executar_QUANDO_id_existe_ENTAO_salva_docente_no_repositorio(self) -> None:
        otd_docente: OTDDocente = FabricaTesteOTDDocente.build()
        docente: Docente = FabricaTesteDocente.build()
        when(OTDDocente).para_entidade().thenReturn(docente)
        when(self.repositorio_docente).id_existe(docente.id).thenReturn(True)
        when(self.repositorio_docente).salvar(docente)

        self.caso_de_uso.executar(otd_docente)

        verify(self.repositorio_docente).salvar(docente)

    def test_executar_QUANDO_id_nao_existe_ENTAO_lanca_erro_docente_nao_encontrado(self) -> None:
        otd_docente: OTDDocente = FabricaTesteOTDDocente.build()
        docente: Docente = FabricaTesteDocente.build()
        when(OTDDocente).para_entidade().thenReturn(docente)
        when(self.repositorio_docente).id_existe(docente.id).thenReturn(False)

        with self.assertRaises(ErroDocenteNaoEncontrado):
            self.caso_de_uso.executar(otd_docente)
