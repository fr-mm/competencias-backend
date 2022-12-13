from random import randint

import factory

from dominio.otds import OTDCursoSaida
from testes.fabricas.dominio.otds.fabrica_teste_otd_modulo import FabricaTesteOTDModulo


class FabricaTesteOTDCursoSaida(factory.Factory):
    class Meta:
        model = OTDCursoSaida

    id = factory.Faker('uuid4', cast_to=None)
    nome = factory.Faker('name')
    modulos = factory.List([factory.SubFactory(FabricaTesteOTDModulo) for _ in range(randint(1, 3))])
    ativo = factory.Faker('pybool')
