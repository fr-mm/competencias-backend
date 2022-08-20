from unittest import TestCase

from dominio.objetos_de_valor import NomeDeDocente
from dominio.otds import OTDEntradaCasoDeUsoCriarDocente
from testes.fabricas.dominio.objetos_de_valor import FabricaTesteNomeDeDocente


class TestOTDEntradaCasoDeUsoCriarDocente(TestCase):
    def test_para_entidade_QUANDO_atributos_validos_ENTAO_retorna_docente_com_atributos_esperados(self) -> None:
        nome = FabricaTesteNomeDeDocente.build().valor
        otd = OTDEntradaCasoDeUsoCriarDocente(
            nome=nome
        )

        docente = otd.para_entidade()

        atributos_resultantes = [
            docente.nome
        ]
        atributos_esperados = [
            NomeDeDocente(nome)
        ]
        self.assertEqual(atributos_resultantes, atributos_esperados)
