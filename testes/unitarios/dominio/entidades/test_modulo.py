from random import randint
from typing import List
from unittest import TestCase
from uuid import uuid4, UUID

from dominio.entidades import Modulo
from dominio.objetos_de_valor import Id, NumeroDeModulo
from testes.fabricas import FabricaTesteId, FabricaTesteNumeroDeModulo


class TestModulo(TestCase):
    def test_construir_QUANDO_atributos_informados_ENTAO_retorna_instancia_com_atributos_esperados(self) -> None:
        id_: Id = FabricaTesteId.build()
        numero: NumeroDeModulo = FabricaTesteNumeroDeModulo.build()
        disciplinas_ids: List[Id] = [FabricaTesteId.build() for _ in range(3)]

        modulo = Modulo.construir(
            id_=id_.valor,
            numero=numero.valor,
            disciplinas_ids=[id_.valor for id_ in disciplinas_ids],
        )

        atributos = [
            modulo.id,
            modulo.numero,
            modulo.disciplinas_ids,
        ]
        esperado = [id_, numero, disciplinas_ids]
        self.assertEqual(atributos, esperado)

    def test_construir_QUANDO_id_nao_informado_ENTAO_gera_novo_id(self) -> None:
        modulo = Modulo.construir(
            numero=2,
            disciplinas_ids=[uuid4() for _ in range(randint(1, 5))],
        )

        self.assertIsInstance(modulo.id.valor, UUID)
