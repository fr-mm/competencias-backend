import factory

from dominio.objetos_de_valor import NomeDeDisciplina


class FabricaTesteNomeDeDisciplina(factory.Factory):
    class Meta:
        model = NomeDeDisciplina

    valor = factory.Faker('name')
