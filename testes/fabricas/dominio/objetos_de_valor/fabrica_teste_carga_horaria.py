import factory

from dominio.objetos_de_valor import CargaHoraria


class FabricaTesteCargaHoraria(factory.Factory):
    class Meta:
        model = CargaHoraria

    valor = factory.Faker('pyint', min_value=1, max_value=1000)
