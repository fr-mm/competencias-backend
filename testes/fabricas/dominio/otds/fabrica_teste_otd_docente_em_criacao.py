import factory

from dominio.otds import OTDDocenteEmCriacao


class FabricaTesteOTDDocenteEmCriacao(factory.Factory):
    class Meta:
        model = OTDDocenteEmCriacao

    nome = factory.Faker('name')
