from unittest import TestCase

from dominio.erros import ErroComprimentoDeNome
from dominio.objetos_de_valor.nome_generico import NomeGenerico
from testes.fabricas import FabricaTesteNomeGenerico


class TestNomeGenerico(TestCase):
    def test_valor_QUANDO_valor_atribuido_ENTAO_retorna_valor(self) -> None:
        valor = 'Foobar'
        nome: NomeGenerico = FabricaTesteNomeGenerico.build(valor=valor)

        resultado = nome.valor

        self.assertEqual(resultado, valor)

    def test_eq_QUANDO_valores_sao_iguais_ENTAO_retorna_true(self) -> None:
        valor = 'Foobar'
        nome1 = FabricaTesteNomeGenerico.build(valor=valor)
        nome2 = FabricaTesteNomeGenerico.build(valor=valor)

        resultado = nome1 == nome2

        self.assertTrue(resultado)

    def test_eq_QUANDO_valores_sao_diferentes_ENTAO_retorna_false(self) -> None:
        nome1 = FabricaTesteNomeGenerico.build(valor='Foobar')
        nome2 = FabricaTesteNomeGenerico.build(valor='Barfoo')

        resultado = nome1 == nome2

        self.assertFalse(resultado)

    def test_validar_init_QUANDO_tamanho_muito_curto_ENTAO_lanca_erro_comprimento_de_nome(self) -> None:
        valor = 'Og'

        with self.assertRaises(ErroComprimentoDeNome):
            FabricaTesteNomeGenerico.build(valor=valor, tamanho_minimo=3)

    def test_validar_init_QUANDO_tamanho_muito_longo_ENTAO_lanca_erro_comprimento_de_nome(self) -> None:
        valor = 'Foobar'

        with self.assertRaises(ErroComprimentoDeNome):
            FabricaTesteNomeGenerico.build(valor=valor, tamanho_maximo=5)
