import factory

from dominio.objetos_de_valor import Email


class FabricaTesteEmail(factory.Factory):

    class Meta:
        model = Email

    valor = factory.Faker('email')
