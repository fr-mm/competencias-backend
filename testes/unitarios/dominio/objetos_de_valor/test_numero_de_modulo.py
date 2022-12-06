from unittest import TestCase

from dominio.objetos_de_valor import NumeroDeModulo


class TestNumeroDeModulo(TestCase):
    def test_valor_QUANDO_valor_chamado_ENTAO_retorna_valor_atribuido(self) -> None:
        valor = 1
        numero_de_modulo = NumeroDeModulo(valor)

        resultado = numero_de_modulo.valor

        self.assertEqual(resultado, valor)

    def test_eq_QUANDO_valores_iguais_ENTAO_retorna_true(self) -> None:
        numero_de_modulo1 = NumeroDeModulo(1)
        numero_de_modulo2 = NumeroDeModulo(1)

        resultado = numero_de_modulo1 == numero_de_modulo2

        self.assertTrue(resultado)

    def test_eq_QUANDO_valores_diferentes_ENTAO_retorna_false(self) -> None:
        numero_de_modulo1 = NumeroDeModulo(1)
        numero_de_modulo2 = NumeroDeModulo(2)

        resultado = numero_de_modulo1 == numero_de_modulo2

        self.assertFalse(resultado)
