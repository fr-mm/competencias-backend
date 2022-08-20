import factory

from dominio.objetos_de_valor import IdDeDocente


class FabricaTesteIdDeDocente(factory.Factory):
    class Meta:
        model = IdDeDocente

    valor = factory.Faker('uuid4')
