from unittest import TestCase

from dominio.erros import ErroEmailInvalido
from dominio.objetos_de_valor import Email


class TestEmail(TestCase):
    def test_init_QUANDO_valor_valido_ENTAO_atribui_valor(self) -> None:
        valor = 'valido@email.com'

        email = Email(valor)

        self.assertEqual(email.valor, valor)

    def test_init_QUANDO_pontos_separando_palavras_ENTAO_atribui_valor(self) -> None:
        valor = 'valor.valido.com.pontos@test.com.ponto.br'

        email = Email(valor)

        self.assertEqual(email.valor, valor)

    def test_init_QUANDO_valor_nao_tem_arroba_ENTAO_lanca_erro_email_invalido(self) -> None:
        valor = 'email.invalido'

        with self.assertRaises(ErroEmailInvalido):
            Email(valor)

    def test_init_QUANDO_arroba_como_primeiro_caracter_ENTAO_lanca_erro_email_invalido(self) -> None:
        valor = '@invalido.com'

        with self.assertRaises(ErroEmailInvalido):
            Email(valor)

    def test_init_QUANDO_arroba_como_ultimo_caracter_ENTAO_lanca_erro_email_invalido(self) -> None:
        valor = 'invalido@'

        with self.assertRaises(ErroEmailInvalido):
            Email(valor)

    def test_init_QUANDO_ponto_como_primeiro_caracter_ENTAO_lanca_erro_email_invalido(self) -> None:
        valor = '.email@invalido.com'

        with self.assertRaises(ErroEmailInvalido):
            Email(valor)

    def test_init_QUANDO_ponto_como_ultimo_caracter_ENTAO_lanca_erro_email_invalido(self) -> None:
        valor = 'email.@invalido.com'

        with self.assertRaises(ErroEmailInvalido):
            Email(valor)
