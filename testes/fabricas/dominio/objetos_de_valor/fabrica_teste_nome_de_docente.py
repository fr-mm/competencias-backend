import factory

from dominio.objetos_de_valor import NomeDeDocente


class FabricaTesteNomeDeDocente(factory.Factory):
    class Meta:
        model = NomeDeDocente

    valor = factory.Faker('name')
