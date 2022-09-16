from random import randint
from unittest import TestCase
from uuid import uuid4

from dominio.objetos_de_valor import IdDeUsuario


class TestIdDeUsuario(TestCase):
    def test_init_QUANDO_valor_informado_ENTAO_atribui_valor(self) -> None:
        valor = randint(0, 64)

        id_de_docente = IdDeUsuario(valor)

        self.assertEqual(id_de_docente.valor, valor)
