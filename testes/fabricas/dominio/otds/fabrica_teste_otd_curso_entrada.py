from random import randint

import factory

from dominio.otds import OTDCursoEntrada
from testes.fabricas.dominio.otds.fabrica_teste_otd_modulo_em_criacao import FabricaTesteOTDModuloEmCriacao


class FabricaTesteOTDCursoEntrada(factory.Factory):
    class Meta:
        model = OTDCursoEntrada

    id = factory.Faker('uuid4', cast_to=None)
    nome = factory.Faker('name')
    modulos = factory.List([factory.SubFactory(FabricaTesteOTDModuloEmCriacao) for _ in range(randint(1, 6))])
    ativo = factory.Faker('pybool')
