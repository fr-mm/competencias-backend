from random import randint

import factory

from dominio.otds import OTDCursoEmCriacao
from testes.fabricas.dominio.otds.fabrica_teste_otd_modulo import FabricaTesteOTDModulo


class FabricaTesteOTDCursoEmCriacao(factory.Factory):
    class Meta:
        model = OTDCursoEmCriacao

    nome = factory.Faker('name')
    modulos = factory.List([factory.SubFactory(FabricaTesteOTDModulo) for _ in range(randint(1, 6))])
    ativo = factory.Faker('pybool')
