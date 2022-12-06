import factory

from dominio.entidades import UnidadeSenai
from testes.fabricas.dominio.objetos_de_valor.fabrica_teste_id import FabricaTesteId
from testes.fabricas.dominio.objetos_de_valor.fabrica_teste_nome_unidade_senai import FabricaTesteNomeUnidadeSenai


class FabricaTesteUnidadeSenai(factory.Factory):
    class Meta:
        model = UnidadeSenai

    id = factory.SubFactory(FabricaTesteId)
    nome = factory.SubFactory(FabricaTesteNomeUnidadeSenai)
