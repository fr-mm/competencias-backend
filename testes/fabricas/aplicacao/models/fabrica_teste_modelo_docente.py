import factory.django

from aplicacao.models import ModeloDocente


class FabricaTesteModeloDocente(factory.django.DjangoModelFactory):
    class Meta:
        model = ModeloDocente

    nome = factory.Faker('name')
    id = factory.Faker('uuid4')
    ativo = factory.Faker('boolean')
