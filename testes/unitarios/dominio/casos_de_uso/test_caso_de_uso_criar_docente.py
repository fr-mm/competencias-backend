from unittest import TestCase
from mockito import mock, unstub, when, verify

from dominio.casos_de_uso import CasoDeUsoCriarDocente
from dominio.entidades import Docente
from dominio.otds import OTDEntradaCasoDeUsoCriarDocente, OTDSaidaCasoDeUsoCriarDocente
from testes.fabricas.dominio.entidades import FabricaTesteDocente
from testes.fabricas.dominio.otds import FabricaTesteOTDEntradaCasoDeUsoCriarDocente


class TestCasoDeUsoCriarDocente(TestCase):
    def setUp(self) -> None:
        self.docente: Docente = FabricaTesteDocente.build()
        self.repositorio_docente = mock({
            'trazer_por_id': lambda id_: self.docente,
            'salvar': lambda docente: None,
            'deletar_por_id': lambda id_: None
        })
        self.caso_de_uso_criar_docente = CasoDeUsoCriarDocente(
            repositorio_docente=self.repositorio_docente
        )

    def tearDown(self) -> None:
        unstub()

    def test_executar_QUANDO_otd_entrada_fornecido_ENTAO_salva_docente_com_atributos_esperados_no_repositorio(self) -> None:
        otd_entrada: OTDEntradaCasoDeUsoCriarDocente = FabricaTesteOTDEntradaCasoDeUsoCriarDocente.build()
        when(otd_entrada).para_entidade().thenReturn(self.docente)
        when(self.repositorio_docente).salvar(self.docente)

        self.caso_de_uso_criar_docente.executar(otd_entrada)

        verify(self.repositorio_docente).salvar(self.docente)

    def test_executar_QUANDO_otd_entrada_fornecido_ENTAO_retorna_otd_saida_esperado(self) -> None:
        otd_entrada: OTDEntradaCasoDeUsoCriarDocente = FabricaTesteOTDEntradaCasoDeUsoCriarDocente.build()
        when(otd_entrada).para_entidade().thenReturn(self.docente)

        otd_saida = self.caso_de_uso_criar_docente.executar(otd_entrada)

        otd_saida_esperado = OTDSaidaCasoDeUsoCriarDocente(
            id=str(self.docente.id.valor),
            nome=self.docente.nome.valor
        )
        self.assertEqual(otd_saida, otd_saida_esperado)
