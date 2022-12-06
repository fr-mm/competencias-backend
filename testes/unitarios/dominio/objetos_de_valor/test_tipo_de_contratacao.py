from unittest import TestCase

from dominio.enums import TipoDeContratacaoEnum
from testes.fabricas import FabricaTesteTipoDeContratacao


class TestTipoDeContratacao(TestCase):

    def test_valor_QUANDO_valor_atribuido_ENTAO_retorna_valor(self) -> None:
        valor = TipoDeContratacaoEnum.HORISTA
        tipo_de_contratacao = FabricaTesteTipoDeContratacao.build(valor=valor.value)

        resultado = tipo_de_contratacao.valor

        self.assertEqual(resultado, valor)

    def test_eq_QUANDO_valores_sao_iguais_ENTAO_retorna_true(self) -> None:
        tipo_de_contratacao1 = FabricaTesteTipoDeContratacao.build()
        tipo_de_contratacao2 = FabricaTesteTipoDeContratacao.build(valor=tipo_de_contratacao1.valor)

        resultado = tipo_de_contratacao1 == tipo_de_contratacao2

        self.assertTrue(resultado)

    def test_eq_QUANDO_valores_sao_diferentes_ENTAO_retorna_false(self) -> None:
        tipo_de_contratacao1 = FabricaTesteTipoDeContratacao.build(valor=TipoDeContratacaoEnum.HORISTA.value)
        tipo_de_contratacao2 = FabricaTesteTipoDeContratacao.build(valor=TipoDeContratacaoEnum.MENSALISTA.value)

        resultado = tipo_de_contratacao1 == tipo_de_contratacao2

        self.assertFalse(resultado)
