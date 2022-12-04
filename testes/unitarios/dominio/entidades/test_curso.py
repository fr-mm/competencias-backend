from random import choice, randint
from typing import List
from unittest import TestCase
from uuid import uuid4, UUID

from dominio.entidades import Curso
from dominio.erros import ErroAoAtivarDesativarEntidade
from dominio.objetos_de_valor import Id, NomeDeCurso
from testes.fabricas import FabricaTesteId, FabricaTesteNomeDeCurso, FabricaTesteCurso


class TestCurso(TestCase):
    def test_construir_QUANDO_atributos_informados_ENTAO_retorna_instancia_com_atributos_esperados(self) -> None:
        id_: Id = FabricaTesteId.build()
        nome: NomeDeCurso = FabricaTesteNomeDeCurso.build()
        modulos_ids: List[Id] = [FabricaTesteId.build() for _ in range(randint(1, 6))]
        ativo = choice([True, False])
        curso = Curso.construir(
            id_=id_.valor,
            nome=nome.valor,
            modulos_ids=[id_.valor for id_ in modulos_ids],
            ativo=ativo
        )

        atributos = [
            curso.id,
            curso.nome,
            curso.modulos_ids,
            curso.ativo
        ]
        esperado = [id_, nome, modulos_ids, ativo]
        self.assertEqual(atributos, esperado)

    def test_construir_QUANDO_id_nao_informado_ENTAO_gera_novo_id(self) -> None:
        curso = Curso.construir(
            nome='Foobar',
            modulos_ids=[uuid4() for _ in range(randint(1, 6))],
            ativo=True
        )

        self.assertIsInstance(curso.id.valor, UUID)

    def test_ativar_QUANDO_desativado_ENTAO_ativa(self) -> None:
        curso: Curso = FabricaTesteCurso.build(ativo=False)

        curso.ativar()

        self.assertTrue(curso.ativo)

    def test_desativar_QUANDO_ativo_ENTAO_desativa(self) -> None:
        curso: Curso = FabricaTesteCurso.build(ativo=True)

        curso.desativar()

        self.assertFalse(curso.ativo)

    def test_ativar_QUANDO_ativo_ENTAO_lanca_erro_ao_ativar_desativar_entidade(self) -> None:
        curso: Curso = FabricaTesteCurso.build(ativo=True)

        with self.assertRaises(ErroAoAtivarDesativarEntidade):
            curso.ativar()

    def test_desativar_QUANDO_desativado_ENTAO_lanca_erro_ao_ativar_desativar_entidade(self) -> None:
        curso: Curso = FabricaTesteCurso.build(ativo=False)

        with self.assertRaises(ErroAoAtivarDesativarEntidade):
            curso.desativar()
