from random import randint

import factory

from dominio.entidades import Modulo
from testes.fabricas.dominio.objetos_de_valor import FabricaTesteId, FabricaTesteNumeroDeModulo
from testes.fabricas.dominio.entidades.fabrica_teste_disciplina import FabricaTesteDisciplina


class FabricaTesteModulo(factory.Factory):
    class Meta:
        model = Modulo

    id_ = factory.SubFactory(FabricaTesteId)
    numero = factory.SubFactory(FabricaTesteNumeroDeModulo)
    disciplinas = factory.List([
        FabricaTesteDisciplina.build() for _ in range(randint(1, 6))
    ])
    ativo = factory.Faker('pybool')
