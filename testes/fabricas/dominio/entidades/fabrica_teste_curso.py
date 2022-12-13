from random import randint

import factory

from dominio.entidades import Curso
from testes.fabricas.dominio.entidades.fabrica_teste_modulo import FabricaTesteModulo
from testes.fabricas.dominio.objetos_de_valor import FabricaTesteId, FabricaTesteNomeDeCurso


class FabricaTesteCurso(factory.Factory):
    class Meta:
        model = Curso

    id_ = factory.SubFactory(FabricaTesteId)
    nome = factory.SubFactory(FabricaTesteNomeDeCurso)
    modulos = factory.List([FabricaTesteModulo.build() for _ in range(randint(1, 6))])
    ativo = factory.Faker('pybool')
