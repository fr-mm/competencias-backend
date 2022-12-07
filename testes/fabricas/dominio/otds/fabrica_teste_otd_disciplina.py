import factory

from dominio.otds import OTDDisciplina


class FabricaTesteOTDDisciplina(factory.Factory):
    class Meta:
        model = OTDDisciplina

    id = factory.Faker('uuid4', cast_to=None)
    nome = factory.Faker('name')
    carga_horaria = factory.Faker('pyint')
    ativo = factory.Faker('pybool')
