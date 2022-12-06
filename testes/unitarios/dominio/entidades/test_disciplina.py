from unittest import TestCase
from uuid import UUID

from dominio.entidades import Disciplina
from dominio.erros import ErroAoAtivarDesativarEntidade
from dominio.objetos_de_valor import NomeDeDisciplina, Id, CargaHoraria
from testes.fabricas import FabricaTesteDisciplina, FabricaTesteNomeDeDisciplina, FabricaTesteCargaHoraria, \
    FabricaTesteId


class TestDisciplina(TestCase):
    def test_construir_QUANDO_valores_validos_ENTAO_retorna_instancia_com_atributos_esperados(self) -> None:
        id_ = FabricaTesteId.build().valor
        nome = FabricaTesteNomeDeDisciplina.build().valor
        carga_horaria = FabricaTesteCargaHoraria.build().valor
        ativo = True

        disciplina = Disciplina.construir(
            id_=id_,
            nome=nome,
            carga_horaria=carga_horaria,
            ativo=ativo
        )

        resultado = [
            disciplina.id,
            disciplina.nome,
            disciplina.carga_horaria,
            disciplina.ativo
        ]
        esperado = [
            Id(id_),
            NomeDeDisciplina(nome),
            CargaHoraria(carga_horaria),
            ativo
        ]
        self.assertEqual(resultado, esperado)

    def test_construir_QUANDO_id_nao_informado_ENTAO_gera_novo_id(self) -> None:
        disciplina = Disciplina.construir(
            nome='Foobar',
            carga_horaria=10,
            ativo=True
        )

        self.assertIsInstance(disciplina.id.valor, UUID)

    def test_ativar_QUANDO_desativado_ENTAO_ativa(self) -> None:
        disciplina: Disciplina = FabricaTesteDisciplina.build(ativo=False)

        disciplina.ativar()

        self.assertTrue(disciplina.ativo)

    def test_ativar_QUANDO_ativo_ENTAO_lanca_erro_ao_ativar_desativar_entidade(self) -> None:
        disciplina: Disciplina = FabricaTesteDisciplina.build(ativo=True)

        with self.assertRaises(ErroAoAtivarDesativarEntidade):
            disciplina.ativar()

    def test_desativar_QUANDO_ativo_ENTAO_desativa(self) -> None:
        disciplina: Disciplina = FabricaTesteDisciplina.build(ativo=True)

        disciplina.desativar()

        self.assertFalse(disciplina.ativo)

    def test_desativar_QUANDO_desativado_ENTAO_lanca_erro_ao_ativar_desativar_entidade(self) -> None:
        disciplina: Disciplina = FabricaTesteDisciplina.build(ativo=False)

        with self.assertRaises(ErroAoAtivarDesativarEntidade):
            disciplina.desativar()
