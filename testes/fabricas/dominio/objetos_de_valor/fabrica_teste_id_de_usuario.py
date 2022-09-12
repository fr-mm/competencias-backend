import factory

from dominio.objetos_de_valor import IdDeUsuario


class FabricaTesteIdDeUsuario(factory.Factory):
    class Meta:
        model = IdDeUsuario

    valor = factory.Faker('uuid4')
