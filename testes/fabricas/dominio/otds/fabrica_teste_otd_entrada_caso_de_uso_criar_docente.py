import factory

from dominio.otds import OTDEntradaCasoDeUsoCriarDocente


class FabricaTesteOTDEntradaCasoDeUsoCriarDocente(factory.Factory):
    class Meta:
        model = OTDEntradaCasoDeUsoCriarDocente

    nome = factory.Faker('name')
