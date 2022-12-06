from unittest import TestCase

from testes.fabricas import FabricaTesteNomeUnidadeSenai


class TestNomeUnidadeSenai(TestCase):

    def test_valor_QUANDO_valor_atribuido_ENTAO_retorna_valor(self) -> None:
        valor = 'Foobar'
        nomeUnidadeSenai = FabricaTesteNomeUnidadeSenai.build(valor=valor)

        resultado = nomeUnidadeSenai.valor

        self.assertEqual(resultado, valor)

    def test_eq_QUANDO_valores_sao_iguais_ENTAO_retorna_true(self) -> None:
        valor = 'Foobar'
        nome1 = FabricaTesteNomeUnidadeSenai.build()
        nome2 = FabricaTesteNomeUnidadeSenai.build(valor=nome1.valor)

        resultado = nome1 == nome2

        self.assertTrue(resultado)

    def test_eq_QUANDO_valores_sao_diferentes_ENTAO_retorna_false(self) -> None:
        nome1 = FabricaTesteNomeUnidadeSenai.build(valor='Foobar')
        nome2 = FabricaTesteNomeUnidadeSenai.build(valor='Barfoo')

        resultado = nome1 == nome2

        self.assertFalse(resultado)
