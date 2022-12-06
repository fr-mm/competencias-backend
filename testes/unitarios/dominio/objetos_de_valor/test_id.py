from unittest import TestCase
from uuid import uuid4

from dominio.objetos_de_valor import Id


class TestId(TestCase):
    def test_init_QUANDO_valor_informado_ENTAO_atribui_valor(self) -> None:
        valor = uuid4()

        id_ = Id(valor)

        self.assertEqual(id_.valor, valor)

    def test_init_QUANDO_valor_nao_informado_ENTAO_atribui_valor_gerado_nao_nulo(self) -> None:
        id_ = Id()

        self.assertIsNotNone(id_.valor)
