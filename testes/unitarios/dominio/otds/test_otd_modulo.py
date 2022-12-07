from unittest import TestCase

from dominio.entidades import Modulo
from dominio.objetos_de_valor import Id, NumeroDeModulo
from dominio.otds import OTDModulo
from testes.fabricas import FabricaTesteOTDModulo, FabricaTesteModulo


class TestOTDModulo(TestCase):
    def test_para_entidade_QUANDO_atributos_validos_ENTAO_retorna_docente_com_atributos_esperados(self) -> None:
        otd: OTDModulo = FabricaTesteOTDModulo.build()

        modulo = otd.para_entidade()

        atributos_resultantes = [
            modulo.id,
            modulo.numero,
            modulo.disciplinas_ids,
        ]
        atributos_esperados = [
            Id(otd.id),
            NumeroDeModulo(otd.numero),
            [Id(id_) for id_ in otd.disciplinas_ids],
        ]
        self.assertEqual(atributos_resultantes, atributos_esperados)

    def test_de_entidade_QUANDO_entidade_informada_ENTAO_retorna_otd_esperado(self) -> None:
        modulo: Modulo = FabricaTesteModulo.build()

        otd = OTDModulo.de_entidade(modulo)

        otd_esperado = OTDModulo(
            id=modulo.id.valor,
            numero=modulo.numero.valor,
            disciplinas_ids=[id_.valor for id_ in modulo.disciplinas_ids],
        )
        self.assertEqual(otd, otd_esperado)
