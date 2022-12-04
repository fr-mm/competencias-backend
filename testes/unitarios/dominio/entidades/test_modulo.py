from random import choice, randint
from typing import List
from unittest import TestCase
from uuid import uuid4, UUID

from dominio.entidades import Modulo
from dominio.erros import ErroAoAtivarDesativarEntidade
from dominio.objetos_de_valor import Id, NumeroDeModulo
from testes.fabricas import FabricaTesteId, FabricaTesteNumeroDeModulo, FabricaTesteModulo


class TestModulo(TestCase):
    def test_construir_QUANDO_atributos_informados_ENTAO_retorna_instancia_com_atributos_esperados(self) -> None:
        id_: Id = FabricaTesteId.build()
        numero: NumeroDeModulo = FabricaTesteNumeroDeModulo.build()
        disciplinas_ids: List[Id] = [FabricaTesteId.build() for _ in range(3)]
        ativo = choice([True, False])

        modulo = Modulo.construir(
            id_=id_.valor,
            numero=numero.valor,
            disciplinas_ids=[id_.valor for id_ in disciplinas_ids],
            ativo=ativo
        )

        atributos = [
            modulo.id,
            modulo.numero,
            modulo.disciplinas_ids,
            modulo.ativo
        ]
        esperado = [id_, numero, disciplinas_ids, ativo]
        self.assertEqual(atributos, esperado)

    def test_construir_QUANDO_id_nao_informado_ENTAO_gera_novo_id(self) -> None:
        modulo = Modulo.construir(
            numero=2,
            disciplinas_ids=[uuid4() for _ in range(randint(1, 5))],
            ativo=True
        )

        self.assertIsInstance(modulo.id.valor, UUID)

    def test_ativar_QUANDO_desativado_ENTAO_ativa(self) -> None:
        modulo: Modulo = FabricaTesteModulo.build(ativo=False)

        modulo.ativar()

        self.assertTrue(modulo.ativo)

    def test_desativar_QUANDO_ativo_ENTAO_desativa(self) -> None:
        modulo: Modulo = FabricaTesteModulo.build(ativo=True)

        modulo.desativar()

        self.assertFalse(modulo.ativo)

    def test_ativar_QUANDO_ativo_ENTAO_lanca_erro_ao_ativar_desativar_entidade(self) -> None:
        modulo: Modulo = FabricaTesteModulo.build(ativo=True)

        with self.assertRaises(ErroAoAtivarDesativarEntidade):
            modulo.ativar()

    def test_desativar_QUANDO_desativado_ENTAO_lanca_erro_ao_ativar_desativar_entidade(self) -> None:
        modulo: Modulo = FabricaTesteModulo.build(ativo=False)

        with self.assertRaises(ErroAoAtivarDesativarEntidade):
            modulo.desativar()
