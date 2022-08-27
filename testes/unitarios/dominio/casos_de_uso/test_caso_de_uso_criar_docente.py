from unittest import TestCase
from mockito import mock, unstub, when, verify

from testes.fabricas import FabricaTesteOTDDocenteEmCriacao, FabricaTesteDocente
from dominio.casos_de_uso import CasoDeUsoCriarDocente
from dominio.entidades import Docente
from dominio.otds import OTDDocenteEmCriacao, OTDDocente


class TestCasoDeUsoCriarDocente(TestCase):
    def setUp(self) -> None:
        self.docente: Docente = FabricaTesteDocente.build()
        self.repositorio_docente = mock({
            'salvar': lambda docente: None,
        })
        self.caso_de_uso_criar_docente = CasoDeUsoCriarDocente(
            repositorio_docente=self.repositorio_docente
        )

    def tearDown(self) -> None:
        unstub()

    def test_executar_QUANDO_otd_entrada_fornecido_ENTAO_salva_docente_com_atributos_esperados_no_repositorio(self) -> None:
        otd_entrada: OTDDocenteEmCriacao = FabricaTesteOTDDocenteEmCriacao.build()
        when(OTDDocenteEmCriacao).para_entidade().thenReturn(self.docente)
        when(self.repositorio_docente).salvar(self.docente)

        self.caso_de_uso_criar_docente.executar(otd_entrada)

        verify(self.repositorio_docente).salvar(self.docente)

    def test_executar_QUANDO_otd_entrada_fornecido_ENTAO_retorna_otd_saida_esperado(self) -> None:
        otd_entrada: OTDDocenteEmCriacao = FabricaTesteOTDDocenteEmCriacao.build()
        when(OTDDocenteEmCriacao).para_entidade().thenReturn(self.docente)

        otd_saida = self.caso_de_uso_criar_docente.executar(otd_entrada)

        otd_saida_esperado = OTDDocente(
            id=self.docente.id.valor,
            nome=self.docente.nome.valor
        )
        self.assertEqual(otd_saida, otd_saida_esperado)
