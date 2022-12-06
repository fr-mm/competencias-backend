from django.test import TestCase

from aplicacao.models import ModeloTelefone
from testes.fabricas import FabricaTesteModeloTelefone, FabricaTesteTelefone


class TestModeloTelefone(TestCase):
    def test_para_objeto_de_valor_QUANDO_chamado_ENTAO_retorna_telefone(self) -> None:
        modelo_telefone: ModeloTelefone = FabricaTesteModeloTelefone.build()

        telefone = modelo_telefone.para_objeto_de_valor()

        esperado = FabricaTesteTelefone.build(valor=modelo_telefone.numero)
        self.assertEqual(telefone, esperado)
