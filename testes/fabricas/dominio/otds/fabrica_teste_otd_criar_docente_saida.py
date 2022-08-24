import factory

from dominio.otds import OTDCriarDocenteSaida


class FabricaTesteOTDCriarDocenteSaida(factory.Factory):
    class Meta:
        model = OTDCriarDocenteSaida

    id = factory.Faker('uuid4')
    nome = factory.Faker('name')
