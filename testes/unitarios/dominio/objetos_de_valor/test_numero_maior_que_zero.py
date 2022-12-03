from unittest import TestCase

from dominio.erros import ErroNumeroInvalido
from testes.fabricas import FabricaTesteNumeroMaiorQueZero


class TestNumeroMaiorQueZero(TestCase):
    def test_init_QUANDO_valor_valido_ENTAO_instancia(self) -> None:
        FabricaTesteNumeroMaiorQueZero.build(valor=1)

    def test_init_QUANDO_valor_menor_que_1_ENTAO_lanca_erro_numero_invalido(self) -> None:
        with self.assertRaises(ErroNumeroInvalido):
            FabricaTesteNumeroMaiorQueZero.build(valor=0)

    def test_init_QUANDO_valor_maior_que_limite_ENTAO_lanca_erro_numero_invalido(self) -> None:
        with self.assertRaises(ErroNumeroInvalido):
            FabricaTesteNumeroMaiorQueZero.build(valor=1000000000)

    def test_eq_QUANDO_valores_iguais_ENTAO_retorna_true(self) -> None:
        numero1 = FabricaTesteNumeroMaiorQueZero.build(valor=1, maximo=3)
        numero2 = FabricaTesteNumeroMaiorQueZero.build(valor=1, maximo=4)

        resultado = numero1 == numero2

        self.assertTrue(resultado)

    def test_eq_QUANDO_valores_diferentes_ENTAO_retorna_false(self) -> None:
        numero1 = FabricaTesteNumeroMaiorQueZero.build(valor=1)
        numero2 = FabricaTesteNumeroMaiorQueZero.build(valor=2)

        resultado = numero1 == numero2

        self.assertFalse(resultado)
