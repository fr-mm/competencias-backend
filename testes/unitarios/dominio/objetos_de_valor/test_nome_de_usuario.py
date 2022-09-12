
from unittest import TestCase

from dominio.erros import ErroNomeMuitoCurto
from dominio.objetos_de_valor import NomeDeUsuario


class TestNomeDeDocente(TestCase):
    def setUp(self) -> None:
        self.valor_valido = 'Valor válido'

    def test_valor_QUANDO_valor_atribuido_ENTAO_retorna_valor(self) -> None:
        nome_de_docente = NomeDeUsuario(self.valor_valido)

        resultado = nome_de_docente.valor

        self.assertEqual(resultado, self.valor_valido)

    def test_eq_QUANDO_valores_sao_iguais_ENTAO_retorna_true(self) -> None:
        nome_de_docente1 = NomeDeUsuario(self.valor_valido)
        nome_de_docente2 = NomeDeUsuario(self.valor_valido)

        resultado = nome_de_docente1 == nome_de_docente2

        self.assertTrue(resultado)

    def test_eq_QUANDO_valores_sao_diferentes_ENTAO_retorna_false(self) -> None:
        nome_de_docente1 = NomeDeUsuario(self.valor_valido)
        nome_de_docente2 = NomeDeUsuario(self.valor_valido + 's')

        resultado = nome_de_docente1 == nome_de_docente2

        self.assertFalse(resultado)

    def test_validar_tamanho_QUANDO_tamanho_invalido_ENTAO_lanca_erro_nome_muito_curto(self) -> None:
        valor_muito_curto = 'Og'

        with self.assertRaises(ErroNomeMuitoCurto):
            NomeDeUsuario(valor_muito_curto)
