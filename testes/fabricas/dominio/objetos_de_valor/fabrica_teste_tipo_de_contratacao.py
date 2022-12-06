import factory
from factory import fuzzy

from dominio.enums import TipoDeContratacaoEnum
from dominio.objetos_de_valor import TipoDeContratacao


class FabricaTesteTipoDeContratacao(factory.Factory):
    class Meta:
        model = TipoDeContratacao

    valor = fuzzy.FuzzyChoice([opcao for opcao in TipoDeContratacaoEnum])
