from unittest import TestCase
from uuid import uuid4, UUID

from dominio.objetos_de_valor import IdDeDocente


class TestIdDeDocente(TestCase):
    def test_init_QUANDO_valor_informado_ENTAO_atribui_valor(self) -> None:
        valor = uuid4()

        id_de_docente = IdDeDocente(valor)

        self.assertEqual(id_de_docente.valor, valor)

    def test_init_QUANDO_valor_nao_informado_ENTAO_atribui_valor_autogerado(self) -> None:
        id_de_docente = IdDeDocente()

        self.assertIsInstance(id_de_docente.valor, UUID)
