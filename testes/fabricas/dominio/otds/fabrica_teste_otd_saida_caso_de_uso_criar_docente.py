import factory

from dominio.otds import OTDSaidaCasoDeUsoCriarDocente


class FabricaTesteOTDSaidaCasoDeUsoCriarDocente(factory.Factory):
    class Meta:
        model = OTDSaidaCasoDeUsoCriarDocente

    id = factory.Faker('uuid4')
    nome = factory.Faker('name')
