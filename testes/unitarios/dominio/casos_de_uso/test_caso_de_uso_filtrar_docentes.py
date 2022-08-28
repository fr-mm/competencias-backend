from unittest import TestCase
from mockito import mock, unstub, when

from dominio.casos_de_uso import CasoDeUsoFiltrarDocentes
from testes.fabricas import FabricaTesteDocente
from dominio.otds import OTDDocente
from dominio.entidades import Docente


class TestCasoDeUsoFiltrarDocentes(TestCase):
    def setUp(self) -> None:
        self.repositorio_docente = mock({
            'trazer': None,
        })
        self.caso_de_uso_trazer_docentes = CasoDeUsoFiltrarDocentes(
            repositorio_docente=self.repositorio_docente
        )

    def tearDown(self) -> None:
        unstub()

    def test_executar_QUANDO_filtros_ativo_true_ENTAO_filtra_docentes_ativos(self) -> None:
        docentes: [Docente] = [FabricaTesteDocente.build(ativo=True) for _ in range(2)]
        when(self.repositorio_docente).filtrar(ativo=True).thenReturn(docentes)

        otds_resultantes = self.caso_de_uso_trazer_docentes.executar()

        otds_esperados = [
            OTDDocente(
                id=docente.id.valor,
                nome=docente.nome.valor,
                ativo=docente.ativo
            ) for docente in docentes
        ]
        self.assertEqual(otds_resultantes, otds_esperados)
