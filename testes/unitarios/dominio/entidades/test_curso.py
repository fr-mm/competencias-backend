from random import choice, randint
from typing import List
from unittest import TestCase

from dominio.entidades import Modulo, Disciplina, Curso
from dominio.erros import ErroAoAtivarDesativarEntidade
from dominio.objetos_de_valor import Id, NumeroDeModulo, NomeDeCurso
from testes.fabricas import FabricaTesteId, FabricaTesteNumeroDeModulo, FabricaTesteDisciplina, FabricaTesteModulo, \
    FabricaTesteNomeDeCurso, FabricaTesteCurso


class TestCurso(TestCase):
    def test_construir_QUANDO_atributos_informados_ENTAO_retorna_instancia_com_atributos_esperados(self) -> None:
        id_: Id = FabricaTesteId.build()
        nome: NomeDeCurso = FabricaTesteNomeDeCurso.build()
        modulos: List[Modulo] = [FabricaTesteModulo.build() for _ in range(randint(1, 6))]
        ativo = choice([True, False])
        curso = Curso.construir(
            id_=id_.valor,
            nome=nome.valor,
            modulos=modulos,
            ativo=ativo
        )

        atributos = [
            curso.id,
            curso.nome,
            curso.modulos,
            curso.ativo
        ]
        esperado = [id_, nome, modulos, ativo]
        self.assertEqual(atributos, esperado)

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
