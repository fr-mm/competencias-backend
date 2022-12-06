import factory

from dominio.objetos_de_valor import NomeUnidadeSenai


class FabricaTesteNomeUnidadeSenai(factory.Factory):
    class Meta:
        model = NomeUnidadeSenai

    valor = factory.Faker('name')
