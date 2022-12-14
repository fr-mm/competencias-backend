from random import randint

import factory

from dominio.otds import OTDCursoEmCriacao
from testes.fabricas.dominio.otds.fabrica_teste_otd_modulo_em_criacao import FabricaTesteOTDModuloEmCriacao


class FabricaTesteOTDCursoEmCriacao(factory.Factory):
    class Meta:
        model = OTDCursoEmCriacao

    nome = factory.Faker('name')
    modulos = factory.List([factory.SubFactory(FabricaTesteOTDModuloEmCriacao) for _ in range(randint(1, 6))])
