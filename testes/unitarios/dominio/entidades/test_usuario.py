from random import choice
from unittest import TestCase

from dominio.entidades import Usuario
from dominio.erros import ErroAoAtivarOuDesativarEntidade
from dominio.objetos_de_valor import IdDeUsuario, Email, NomeDeUsuario
from testes.fabricas import FabricaTesteIdDeUsuario, FabricaTesteNomeDeUsuario, FabricaTesteEmail, FabricaTesteUsuario


class TestUsuario(TestCase):
    def test_construir_QUANDO_atributos_validos_ENTAO_atribui_atributos(self) -> None:
        id_: IdDeUsuario = FabricaTesteIdDeUsuario.build()
        nome: NomeDeUsuario = FabricaTesteNomeDeUsuario.build()
        email: Email = FabricaTesteEmail.build()
        ativo = choice([True, False])

        usuario = Usuario.construir(
            id_=id_.valor,
            nome=nome.valor,
            email=email.valor,
            ativo=ativo
        )

        atributos_resultantes = [
            usuario.id,
            usuario.nome,
            usuario.email,
            usuario.ativo
        ]
        atributos_esperados = [
            id_,
            nome,
            email,
            ativo
        ]
        self.assertEqual(atributos_resultantes, atributos_esperados)

    def test_ativar_QUANDO_inativo_ENTAO_ativa_usuario(self) -> None:
        usuario: Usuario = FabricaTesteUsuario.build(ativo=False)

        usuario.ativar()

        self.assertTrue(usuario.ativo)

    def test_ativar_QUANDO_ativo_ENTAO_lanca_erro_ao_ativar_ou_desativar_entidade(self) -> None:
        usuario: Usuario = FabricaTesteUsuario.build(ativo=True)

        with self.assertRaises(ErroAoAtivarOuDesativarEntidade):
            usuario.ativar()

    def test_desativar_QUANDO_ativo_ENTAO_desativa_usuario(self) -> None:
        usuario: Usuario = FabricaTesteUsuario.build(ativo=True)

        usuario.desativar()

        self.assertFalse(usuario.ativo)

    def test_desativar_QUANDO_desaativado_ENTAO_lanca_erro_ao_ativar_ou_desativar_entidade(self) -> None:
        usuario: Usuario = FabricaTesteUsuario.build(ativo=False)

        with self.assertRaises(ErroAoAtivarOuDesativarEntidade):
            usuario.desativar()
