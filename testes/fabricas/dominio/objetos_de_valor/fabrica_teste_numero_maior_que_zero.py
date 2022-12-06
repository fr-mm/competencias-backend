import factory

from dominio.objetos_de_valor import NumeroMaiorQueZero


class FabricaTesteNumeroMaiorQueZero(factory.Factory):
    class Meta:
        model = NumeroMaiorQueZero

    valor = factory.Faker('pyint', min_value=1, max_value=100000)
    maximo = 1000
