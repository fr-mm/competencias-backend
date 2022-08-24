import factory

from dominio.otds import OTDCriarDocenteEntrada


class FabricaTesteOTDCriarDocenteEntrada(factory.Factory):
    class Meta:
        model = OTDCriarDocenteEntrada

    nome = factory.Faker('name')
