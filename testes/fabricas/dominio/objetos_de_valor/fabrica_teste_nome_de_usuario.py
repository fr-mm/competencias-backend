import factory

from dominio.objetos_de_valor import NomeDeUsuario


class FabricaTesteNomeDeUsuario(factory.Factory):
    class Meta:
        model = NomeDeUsuario

    valor = factory.Faker('name')
