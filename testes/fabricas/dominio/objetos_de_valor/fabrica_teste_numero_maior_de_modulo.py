import factory

from dominio.objetos_de_valor import NumeroDeModulo


class FabricaTesteNumeroDeModulo(factory.Factory):
    class Meta:
        model = NumeroDeModulo

    valor = factory.Faker('pyint', min_value=1, max_value=20)
