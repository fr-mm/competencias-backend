from unittest import TestCase
from mockito import mock, unstub, when

from dominio.casos_de_uso import CasoDeUsoTrazerDocente
from testes.fabricas import FabricaTesteDocente
from dominio.otds import OTDDocente
from dominio.entidades import Docente


class TestCasoDeUsoTrazerDocente(TestCase):
    def setUp(self) -> None:
        self.repositorio_docente = mock({
            'trazer_por_id': None,
        })
        self.caso_de_uso_trazer_docente = CasoDeUsoTrazerDocente(
            repositorio_docente=self.repositorio_docente
        )

    def tearDown(self) -> None:
        unstub()

    def test_executar_QUANDO_docente_existe_ENTAO_retorna_otd_esperado(self) -> None:
        docente: Docente = FabricaTesteDocente.build()
        when(self.repositorio_docente).trazer_por_id(docente.id).thenReturn(docente)
        when(self.repositorio_docente).id_existe(docente.id).thenReturn(True)

        otd_resultante = self.caso_de_uso_trazer_docente.executar(docente.id.valor)

        otd_esperado = OTDDocente(
            id=docente.id.valor,
            nome=docente.nome.valor,
            ativo=docente.ativo
        )
        self.assertEqual(otd_resultante, otd_esperado)
