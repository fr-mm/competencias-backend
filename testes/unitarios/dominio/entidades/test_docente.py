from random import getrandbits
from unittest import TestCase

from testes.fabricas import FabricaTesteNomeDeDocente, FabricaTesteId, FabricaTesteDocente
from dominio.erros import ErroAtivarDesativarDocente
from dominio.entidades import Docente
from dominio.objetos_de_valor import Id, NomeDeDocente


class TestDocente(TestCase):
    def test_construir_QUANDO_id_informado_ENTAO_atribui_id(self) -> None:
        nome = FabricaTesteNomeDeDocente.build().valor
        id_ = FabricaTesteId.build().valor

        docente = Docente.construir(
            nome=nome,
            id_=id_
        )

        self.assertEqual(docente.id.valor, id_)

    def test_construir_QUANDO_id_nao_informado_ENTAO_atribui_id_gerado_nao_nulo(self) -> None:
        nome = FabricaTesteNomeDeDocente.build().valor

        docente = Docente.construir(
            nome=nome
        )
        self.assertIsNotNone(docente.id.valor)

    def test_construir_QUANDO_ativo_nao_informado_ENTAO_atribui_true(self) -> None:
        nome = FabricaTesteNomeDeDocente.build().valor

        docente = Docente.construir(
            nome=nome
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

        with self.assertRaises(ErroAtivarDesativarDocente):
            docente.ativar()

    def test_desativar_QUANDO_docente_esta_ativo_ENTAO_inativa_docente(self) -> None:
        docente: Docente = FabricaTesteDocente.build(ativo=True)

        docente.desativar()

        self.assertFalse(docente.ativo)

    def test_desativar_QUANDO_docente_esta_inativo_ENTAO_lanca_erro_ativar_desativar_docente(self) -> None:
        docente: Docente = FabricaTesteDocente.build(ativo=False)

        with self.assertRaises(ErroAtivarDesativarDocente):
            docente.desativar()
