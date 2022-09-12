import factory

from aplicacao.models import ModeloUsuario


class FabricaTesteModeloUsuario(factory.Factory):
    class Meta:
        model = ModeloUsuario

    id = factory.Faker('uuid4')
    username = factory.Faker('name')
    email = factory.Faker('email')
    is_active = factory.Faker('boolean')
