import factory

from dominio.objetos_de_valor import Id


class FabricaTesteId(factory.Factory):
    class Meta:
        model = Id

    valor = factory.Faker('uuid4')
