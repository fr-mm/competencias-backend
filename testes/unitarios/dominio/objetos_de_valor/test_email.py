from unittest import TestCase

from dominio.erros import ErroEmail
from testes.fabricas import FabricaTesteEmail


class TestEmail(TestCase):

    def test_valor_QUANDO_valor_atribuido_ENTAO_retorna_valor(self) -> None:
        valor = 'qualquercoisa@outra.com'
        email = FabricaTesteEmail.build(valor=valor)

        resultado = email.valor

        self.assertEqual(resultado, valor)

    def test_init_QUANDO_email_do_senai_ENTAO_instancia(self) -> None:
        valor = 'rafael.vecchi@ba.estudante.senai.br'
        email = FabricaTesteEmail.build(valor=valor)

        resultado = email.valor

        self.assertEqual(resultado, valor)

    def test_eq_QUANDO_valores_sao_iguais_ENTAO_retorna_true(self) -> None:
        email1 = FabricaTesteEmail.build()
        email2 = FabricaTesteEmail.build(valor=email1.valor)

        resultado = email1 == email2

        self.assertTrue(resultado)

    def test_eq_QUANDO_valores_sao_diferentes_ENTAO_retorna_false(self) -> None:
        email1 = FabricaTesteEmail.build(valor='Foobar@exemplo.com')
        email2 = FabricaTesteEmail.build(valor='Barfoo@exemplo.com')

        resultado = email1 == email2

        self.assertFalse(resultado)

    def test_init_QUANDO_email_invalido_ENTAO_lanca_erro_email(self) -> None:
        valor = 'algo@outro.'

        with self.assertRaises(ErroEmail):
            FabricaTesteEmail.build(valor=valor)
