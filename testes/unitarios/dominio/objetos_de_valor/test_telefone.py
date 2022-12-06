from unittest import TestCase

from dominio.erros import ErroTelefone
from testes.fabricas import FabricaTesteTelefone


class TestTelefone(TestCase):

    def test_valor_QUANDO_valor_atribuido_ENTAO_retorna_valor(self) -> None:
        valor = '(71)99234-1942'
        telefone = FabricaTesteTelefone.build(valor=valor)

        resultado = telefone.valor

        self.assertEqual(resultado, valor)

    def test_eq_QUANDO_valores_sao_iguais_ENTAO_retorna_true(self) -> None:
        telefone1 = FabricaTesteTelefone.build()
        telefone2 = FabricaTesteTelefone.build(valor=telefone1.valor)

        resultado = telefone1 == telefone2

        self.assertTrue(resultado)

    def test_eq_QUANDO_valores_sao_diferentes_ENTAO_retorna_false(self) -> None:
        telefone1 = FabricaTesteTelefone.build(valor='(71)98761-9887')
        telefone2 = FabricaTesteTelefone.build(valor='(71)97987-7676')

        resultado = telefone1 == telefone2

        self.assertFalse(resultado)

    def test_init_QUANDO_telefone_invalido_ENTAO_lanca_erro_telefone(self) -> None:
        valor = '(71)9898989898'

        with self.assertRaises(ErroTelefone):
            FabricaTesteTelefone.build(valor=valor)
