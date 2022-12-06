from unittest import TestCase

from testes.fabricas import FabricaTesteOTDDocenteEmCriacao
from dominio.otds import OTDDocenteEmCriacao
from dominio.objetos_de_valor import NomeDeDocente, Id, TipoDeContratacao, Telefone, Email


class TestOTDDocenteEmCriacao(TestCase):
    def test_para_entidade_QUANDO_atributos_validos_ENTAO_retorna_docente_com_atributos_esperados(self) -> None:
        otd: OTDDocenteEmCriacao = FabricaTesteOTDDocenteEmCriacao.build()

        docente = otd.para_entidade()

        atributos_resultantes = [
            docente.nome,
            docente.email,
            docente.telefones,
            docente.tipo_de_contratacao,
            docente.unidade_senai_id,
        ]
        atributos_esperados = [
            NomeDeDocente(otd.nome),
            Email(otd.email),
            [Telefone(telefone) for telefone in otd.telefones],
            TipoDeContratacao(otd.tipo_de_contratacao),
            Id(otd.unidade_senai_id),
        ]
        self.assertEqual(atributos_resultantes, atributos_esperados)
