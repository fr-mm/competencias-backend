import factory

from aplicacao.models import ModeloDisciplina


class FabricaTesteModeloDisciplina(factory.django.DjangoModelFactory):
    class Meta:
        model = ModeloDisciplina

    id = factory.Faker('uuid4', cast_to=None)
    nome = factory.Faker('name')
    carga_horaria = factory.Faker('pyint', min_value=1, max_value=200)
    ativo = factory.Faker('pybool')
