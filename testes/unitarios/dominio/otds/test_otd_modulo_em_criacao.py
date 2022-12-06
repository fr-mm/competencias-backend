from unittest import TestCase

from dominio.objetos_de_valor import Id, NumeroDeModulo
from dominio.otds import OTDModulo
from testes.fabricas import FabricaTesteOTDModulo


class TestOTDModulo(TestCase):
    def test_para_entidade_QUANDO_atributos_validos_ENTAO_retorna_docente_com_atributos_esperados(self) -> None:
        otd: OTDModulo = FabricaTesteOTDModulo.build()

        modulo = otd.para_entidade()

        atributos_resultantes = [
            modulo.numero,
            modulo.disciplinas_ids,
            modulo.ativo
        ]
        atributos_esperados = [
            NumeroDeModulo(otd.numero),
            [Id(id_) for id_ in otd.disciplinas_ids],
            otd.ativo
        ]
        self.assertEqual(atributos_resultantes, atributos_esperados)
