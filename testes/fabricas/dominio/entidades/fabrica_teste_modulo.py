from random import randint

import factory

from dominio.entidades import Modulo
from testes.fabricas.dominio.objetos_de_valor import FabricaTesteId, FabricaTesteNumeroDeModulo


class FabricaTesteModulo(factory.Factory):
    class Meta:
        model = Modulo

    id_ = factory.SubFactory(FabricaTesteId)
    numero = factory.SubFactory(FabricaTesteNumeroDeModulo)
    disciplinas_ids = factory.List([
        FabricaTesteId.build() for _ in range(randint(1, 6))
    ])
    ativo = factory.Faker('pybool')
