from unittest import TestCase

from dominio.entidades import Docente
from dominio.otds import OTDSaidaCasoDeUsoCriarDocente
from testes.fabricas.dominio.entidades import FabricaTesteDocente


class TestOTDSaidaCasoDeUsoCriarDocente(TestCase):
    def test_de_entidade_QUANDO_entidade_informada_ENTAO_retorna_otd_com_atributos_esperados(self) -> None:
        docente: Docente = FabricaTesteDocente.build()

        otd = OTDSaidaCasoDeUsoCriarDocente.de_entidade(docente)

        atributos_resultantes = [
            otd.id,
            otd.nome
        ]
        atributos_esperados = [
            str(docente.id.valor),
            docente.nome.valor
        ]
        self.assertEqual(atributos_resultantes, atributos_esperados)
