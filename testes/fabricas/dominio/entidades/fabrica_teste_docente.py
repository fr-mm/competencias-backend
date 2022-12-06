from random import randint

import factory
from factory import fuzzy

from dominio.enums import TipoDeContratacaoEnum
from testes.fabricas.auxiliares import GerarTelefone
from testes.fabricas.dominio.objetos_de_valor import FabricaTesteNomeDeDocente, FabricaTesteId, \
    FabricaTesteEmail, FabricaTesteTelefone, FabricaTesteTipoDeContratacao
from dominio.entidades import Docente


class FabricaTesteDocente(factory.Factory):
    class Meta:
        model = Docente

    nome = factory.SubFactory(FabricaTesteNomeDeDocente)
    id_ = factory.SubFactory(FabricaTesteId)
    email = factory.SubFactory(FabricaTesteEmail)
    telefones = factory.List(
        [FabricaTesteTelefone.build(valor=GerarTelefone.gerar()) for _ in range(randint(1, 5))]
    )
    tipo_de_contratacao = fuzzy.FuzzyChoice(
        [FabricaTesteTipoDeContratacao.build(valor=opcao.value) for opcao in TipoDeContratacaoEnum]
    )
    unidade_senai_id = factory.SubFactory(FabricaTesteId)
    ativo = factory.Faker('boolean')
