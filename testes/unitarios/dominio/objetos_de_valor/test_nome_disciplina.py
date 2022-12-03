from unittest import TestCase

from dominio.objetos_de_valor import NomeDeDisciplina


class TestNomeDisciplina(TestCase):
    def test_valor_QUANDO_valor_valido_ENTAO_retorna_valor(self) -> None:
        valor = 'Foobar'
        nome = NomeDeDisciplina(valor)

        resultado = nome.valor

        self.assertEqual(resultado, valor)

    def test_eq_QUANDO_valores_iguais_ENTAO_retorna_true(self) -> None:
        valor = 'Foobar'
        nome1 = NomeDeDisciplina(valor)
        nome2 = NomeDeDisciplina(valor)

        resultado = nome1 == nome2

        self.assertTrue(resultado)

    def test_eq_QUANDO_valores_diferentes_ENTAO_retorna_false(self) -> None:
        nome1 = NomeDeDisciplina('Foobar')
        nome2 = NomeDeDisciplina('Barfoo')

        resultado = nome1 == nome2

        self.assertFalse(resultado)
