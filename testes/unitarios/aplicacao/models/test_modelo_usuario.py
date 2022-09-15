from uuid import UUID

from django.test import TestCase

from aplicacao.models import ModeloUsuario
from dominio.entidades import Usuario
from testes.fabricas import FabricaTesteUsuario, FabricaTesteModeloUsuario


class TestModeloUsuario(TestCase):
    def test_de_entidade_QUANDO_entidade_fornacida_ENTAO_retorna_modelo_com_atributos_esperados(self) -> None:
        entidade: Usuario = FabricaTesteUsuario.build()

        modelo = ModeloUsuario.de_entidade(entidade)

        atributos_resultantes = [
            modelo.id,
            modelo.nome,
            modelo.email,
            modelo.ativo
        ]
        atributos_esperados = [
            entidade.id.valor,
            entidade.nome.valor,
            entidade.email.valor,
            entidade.ativo
        ]
        self.assertEqual(atributos_resultantes, atributos_esperados)

    def test_para_entidade_QUANDO_chamado_ENTAO_retorna_entidade_com_atributos_esperados(self) -> None:
        modelo: ModeloUsuario = FabricaTesteModeloUsuario.build()

        entidade = modelo.para_entidade()

        atributos_resultantes = [
            entidade.id.valor,
            entidade.nome.valor,
            entidade.email.valor,
            entidade.ativo
        ]
        atributos_esperados = [
            UUID(modelo.id),
            modelo.nome,
            modelo.email,
            modelo.ativo
        ]
        self.assertEqual(atributos_resultantes, atributos_esperados)
