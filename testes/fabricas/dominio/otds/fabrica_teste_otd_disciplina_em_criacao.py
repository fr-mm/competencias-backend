import factory

from dominio.otds import OTDDisciplinaEmCriacao


class FabricaTesteOTDDisciplinaEmCriacao(factory.Factory):
    class Meta:
        model = OTDDisciplinaEmCriacao

    nome = factory.Faker('name')
    carga_horaria = factory.Faker('pyint')
