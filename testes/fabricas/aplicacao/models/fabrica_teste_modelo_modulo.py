import factory.django

from aplicacao.models import ModeloModulo


class FabricaTesteModeloModulo(factory.django.DjangoModelFactory):
    class Meta:
        model = ModeloModulo

    id = factory.Faker('uuid4', cast_to=None)
    numero = factory.Faker('pyint', min_value=1, max_value=4)
