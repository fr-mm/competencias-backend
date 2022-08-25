from unittest import TestCase

from dominio.objetos_de_valor import IdDeDocente, NomeDeDocente
from dominio.entidades import Docente
from dominio.otds import OTDDocente
from testes.fabricas import FabricaTesteOTDDocente, FabricaTesteDocente


class TestOTDDocente(TestCase):
    def test_para_entidade_QUANDO_atributos_validos_ENTAO_retorna_docente_esperado(self) -> None:
        otd: OTDDocente = FabricaTesteOTDDocente.build()

        docente_resultante = otd.para_entidade()

        docente_esperado = Docente(
            id=IdDeDocente(otd.id),
            nome=NomeDeDocente(otd.nome)
        )
        self.assertEqual(docente_resultante, docente_esperado)

    def test_de_entidade_QUANDO_entidade_informada_ENTAO_retorna_otd_esperado(self) -> None:
        docente: Docente = FabricaTesteDocente.build()

        otd = OTDDocente.de_entidade(docente)

        otd_esperado = OTDDocente(
            id=docente.id.valor,
            nome=docente.nome.valor
        )
        self.assertEqual(otd, otd_esperado)
