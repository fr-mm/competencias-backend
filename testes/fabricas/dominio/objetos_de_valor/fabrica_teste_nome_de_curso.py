import factory

from dominio.objetos_de_valor import NomeDeCurso


class FabricaTesteNomeDeCurso(factory.Factory):
    class Meta:
        model = NomeDeCurso

    valor = factory.Faker('name')
