import factory

from dominio.otds import OTDDocente


class FabricaTesteOTDDocente(factory.Factory):
    class Meta:
        model = OTDDocente

    id = factory.Faker('uuid4')
    nome = factory.Faker('name')
