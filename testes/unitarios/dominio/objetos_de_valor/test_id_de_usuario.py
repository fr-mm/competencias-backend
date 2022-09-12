from unittest import TestCase
from uuid import uuid4

from dominio.objetos_de_valor import IdDeUsuario


class TestIdDeUsuario(TestCase):
    def test_init_QUANDO_valor_informado_ENTAO_atribui_valor(self) -> None:
        valor = uuid4()

        id_de_docente = IdDeUsuario(valor)

        self.assertEqual(id_de_docente.valor, valor)

    def test_init_QUANDO_valor_nao_informado_ENTAO_atribui_valor_gerado_nao_nulo(self) -> None:
        id_de_docente = IdDeUsuario()

        self.assertIsNotNone(id_de_docente.valor)
