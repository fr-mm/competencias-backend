from random import getrandbits, randint, choice
from unittest import TestCase

from dominio.entidades import Docente
from dominio.erros import ErroAoAtivarDesativarEntidade
from dominio.objetos_de_valor import Id, NomeDeDocente
from testes.fabricas import FabricaTesteEmail, \
    FabricaTesteTelefone, FabricaTesteTipoDeContratacao
from testes.fabricas import FabricaTesteNomeDeDocente, FabricaTesteId, FabricaTesteDocente


class TestDocente(TestCase):
    def test_construir_QUANDO_atributos_validos_ENTAO_retorna_instancia_com_atributos_esperados(self) -> None:
        nome = FabricaTesteNomeDeDocente.build()
        id_ = FabricaTesteId.build()
        email = FabricaTesteEmail.build()
        telefones = [FabricaTesteTelefone.build() for _ in range(randint(1, 5))]
        tipo_de_contratacao = FabricaTesteTipoDeContratacao.build()
        unidade_senai_id = FabricaTesteId.build()
        ativo = choice([True, False])

        docente = Docente.construir(
            nome=nome.valor,
            id_=id_.valor,
            email=email.valor,
            telefones=[telefone.valor for telefone in telefones],
            tipo_de_contratacao=tipo_de_contratacao.valor,
            unidade_senai_id=unidade_senai_id.valor,
            ativo=ativo
        )

        atributos = [
            docente.nome,
            docente.id,
            docente.email,
            docente.telefones,
            docente.tipo_de_contratacao,
            docente.unidade_senai_id,
            docente.ativo
        ]
        esperado = [
            nome,
            id_,
            email,
            telefones,
            tipo_de_contratacao,
            unidade_senai_id,
            ativo
        ]
        self.assertEqual(atributos, esperado)

    def test_construir_QUANDO_id_nao_informado_ENTAO_atribui_id_gerado_nao_nulo(self) -> None:
        nome = FabricaTesteNomeDeDocente.build()
        email = FabricaTesteEmail.build()
        telefones = [FabricaTesteTelefone.build() for _ in range(randint(1, 5))]
        tipo_de_contratacao = FabricaTesteTipoDeContratacao.build()
        unidade_senai_id = FabricaTesteId.build()
        ativo = choice([True, False])
        docente = Docente.construir(
            nome=nome.valor,
            email=email.valor,
            telefones=[telefone.valor for telefone in telefones],
            tipo_de_contratacao=tipo_de_contratacao.valor,
            unidade_senai_id=unidade_senai_id.valor,
            ativo=ativo
        )

        self.assertIsNotNone(docente.id.valor)

    def test_construir_QUANDO_ativo_nao_informado_ENTAO_atribui_true(self) -> None:
        nome = FabricaTesteNomeDeDocente.build()
        id_ = FabricaTesteId.build()
        email = FabricaTesteEmail.build()
        telefones = [FabricaTesteTelefone.build() for _ in range(randint(1, 5))]
        tipo_de_contratacao = FabricaTesteTipoDeContratacao.build()
        unidade_senai_id = FabricaTesteId.build()

        docente = Docente.construir(
            nome=nome.valor,
            id_=id_.valor,
            email=email.valor,
            telefones=[telefone.valor for telefone in telefones],
            tipo_de_contratacao=tipo_de_contratacao.valor,
            unidade_senai_id=unidade_senai_id.valor,
        )

        self.assertTrue(docente.ativo)

    def test_id_QUANDO_chamado_ENTAO_retorna_id_atribuido(self) -> None:
        id_esperado: Id = FabricaTesteId.build()
        docente: Docente = FabricaTesteDocente.build(id_=id_esperado)

        id_resultante = docente.id

        self.assertEqual(id_resultante, id_esperado)

    def test_nome_QUANDO_chamado_ENTAO_retorna_nome_atribuido(self) -> None:
        nome_esperado: NomeDeDocente = FabricaTesteNomeDeDocente.build()
        docente: Docente = FabricaTesteDocente.build(nome=nome_esperado)

        nome_resultante = docente.nome

        self.assertEqual(nome_resultante, nome_esperado)

    def test_ativo_QUANDOO_chamado_ENTAO_retorna_valor_atribuido(self) -> None:
        valor_esperado = bool(getrandbits(1))
        docente: Docente = FabricaTesteDocente.build(ativo=valor_esperado)

        valor_resultante = docente.ativo

        self.assertEqual(valor_resultante, valor_esperado)

    def test_ativar_QUANDO_docente_esta_inativo_ENTAO_ativa_docente(self) -> None:
        docente: Docente = FabricaTesteDocente.build(ativo=False)

        docente.ativar()

        self.assertTrue(docente.ativo)

    def test_ativar_QUANDO_docente_esta_ativo_ENTAO_lanca_erro_ativar_desativar_docente(self) -> None:
        docente: Docente = FabricaTesteDocente.build(ativo=True)

        with self.assertRaises(ErroAoAtivarDesativarEntidade):
            docente.ativar()

    def test_desativar_QUANDO_docente_esta_ativo_ENTAO_inativa_docente(self) -> None:
        docente: Docente = FabricaTesteDocente.build(ativo=True)

        docente.desativar()

        self.assertFalse(docente.ativo)

    def test_desativar_QUANDO_docente_esta_inativo_ENTAO_lanca_erro_ativar_desativar_docente(self) -> None:
        docente: Docente = FabricaTesteDocente.build(ativo=False)

        with self.assertRaises(ErroAoAtivarDesativarEntidade):
            docente.desativar()
