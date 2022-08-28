from unittest import TestCase
from uuid import UUID

from testes.fabricas import FabricaTesteOTDDocente, FabricaTesteDocente
from dominio.otds import OTDDocente
from dominio.entidades import Docente
from dominio.objetos_de_valor import IdDeDocente, NomeDeDocente


class TestOTDDocente(TestCase):
    def test_para_entidade_QUANDO_atributos_validos_ENTAO_retorna_docente_com_atributos_esperados(self) -> None:
        otd: OTDDocente = FabricaTesteOTDDocente.build()

        docente = otd.para_entidade()

        atributos_resultantes = [
            docente.id,
            docente.nome,
            docente.ativo
        ]
        atributos_esperados = [
            IdDeDocente(otd.id),
            NomeDeDocente(otd.nome),
            otd.ativo
        ]
        self.assertEqual(atributos_resultantes, atributos_esperados)

    def test_de_entidade_QUANDO_entidade_informada_ENTAO_retorna_otd_esperado(self) -> None:
        docente: Docente = FabricaTesteDocente.build()

        otd = OTDDocente.de_entidade(docente)

        otd_esperado = OTDDocente(
            id=docente.id.valor,
            nome=docente.nome.valor,
            ativo=otd.ativo
        )
        self.assertEqual(otd, otd_esperado)
