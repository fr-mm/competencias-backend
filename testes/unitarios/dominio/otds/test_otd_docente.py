from unittest import TestCase

from testes.fabricas import FabricaTesteOTDDocente, FabricaTesteDocente
from dominio.otds import OTDDocente
from dominio.entidades import Docente
from dominio.objetos_de_valor import Id, NomeDeDocente, Email, Telefone, TipoDeContratacao


class TestOTDDocente(TestCase):
    def test_para_entidade_QUANDO_atributos_validos_ENTAO_retorna_docente_com_atributos_esperados(self) -> None:
        otd: OTDDocente = FabricaTesteOTDDocente.build()

        docente = otd.para_entidade()

        atributos_resultantes = [
            docente.id,
            docente.nome,
            docente.email,
            docente.telefones,
            docente.tipo_de_contratacao,
            docente.unidade_senai_id,
            docente.ativo
        ]
        atributos_esperados = [
            Id(otd.id),
            NomeDeDocente(otd.nome),
            Email(otd.email),
            [Telefone(telefone) for telefone in otd.telefones],
            TipoDeContratacao(otd.tipo_de_contratacao),
            Id(otd.unidade_senai_id),
            otd.ativo
        ]
        self.assertEqual(atributos_resultantes, atributos_esperados)

    def test_de_entidade_QUANDO_entidade_informada_ENTAO_retorna_otd_esperado(self) -> None:
        docente: Docente = FabricaTesteDocente.build()
        print(docente.unidade_senai_id)

        otd = OTDDocente.de_entidade(docente)

        otd_esperado = OTDDocente(
            id=docente.id.valor,
            nome=docente.nome.valor,
            email=docente.email.valor,
            telefones=[telefone.valor for telefone in docente.telefones],
            tipo_de_contratacao=str(docente.tipo_de_contratacao.valor.value),
            unidade_senai_id=docente.unidade_senai_id.valor,
            ativo=otd.ativo
        )
        self.assertEqual(otd, otd_esperado)
