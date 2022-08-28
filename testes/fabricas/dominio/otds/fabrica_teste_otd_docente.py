import factory

from dominio.otds import OTDDocente


class FabricaTesteOTDDocente(factory.Factory):
    class Meta:
        model = OTDDocente

    id = factory.Faker('uuid4', cast_to=None)
    nome = factory.Faker('name')
    ativo = factory.Faker('boolean')
