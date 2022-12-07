import factory.django

from aplicacao.models import ModeloCurso


class FabricaTesteModeloCurso(factory.django.DjangoModelFactory):
    class Meta:
        model = ModeloCurso

    id = factory.Faker('uuid4', cast_to=None)
    nome = factory.Faker('name')
    ativo = factory.Faker('pybool')
