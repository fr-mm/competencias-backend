import factory
from factory import fuzzy

from dominio.enums import TipoDeContratacaoEnum
from dominio.otds import OTDDocenteEmCriacao
from testes.fabricas.auxiliares import GerarTelefone


class FabricaTesteOTDDocenteEmCriacao(factory.Factory):
    class Meta:
        model = OTDDocenteEmCriacao

    nome = factory.Faker('name')
    email = factory.Faker('email')
    telefones = factory.List([GerarTelefone.gerar() for _ in range(3)])
    tipo_de_contratacao = fuzzy.FuzzyChoice([opcao.value for opcao in TipoDeContratacaoEnum])
    unidade_senai_id = factory.Faker('uuid4')
