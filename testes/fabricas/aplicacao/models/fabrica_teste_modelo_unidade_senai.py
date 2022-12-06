import factory.django

from aplicacao.models import ModeloUnidadeSenai


class FabricaTesteModeloUnidadeSenai(factory.django.DjangoModelFactory):
    class Meta:
        model = ModeloUnidadeSenai

    id = factory.Faker('uuid4', cast_to=None)
    nome = factory.Faker('name')
