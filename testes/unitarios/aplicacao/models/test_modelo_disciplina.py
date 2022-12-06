from django.test import TestCase

from aplicacao.models import ModeloDisciplina
from dominio.entidades import Disciplina
from testes.fabricas import FabricaTesteModeloDisciplina, FabricaTesteDisciplina


class TestModeloDisciplina(TestCase):
    def test_para_entidade_QUANDO_chamado_ENTAO_retorna_entidade_com_atributos_esperados(self) -> None:
        modelo_disciplina: ModeloDisciplina = FabricaTesteModeloDisciplina.build()

        disciplina = modelo_disciplina.para_entidade()

        atributos = [
            disciplina.id.valor,
            disciplina.nome.valor,
            disciplina.carga_horaria.valor,
            disciplina.ativo
        ]
        esperados = [
            modelo_disciplina.id,
            modelo_disciplina.nome,
            modelo_disciplina.carga_horaria,
            modelo_disciplina.ativo
        ]
        self.assertEqual(atributos, esperados)

    def test_de_entidade_QUANDO_entidade_informada_ENTAO_retorna_modelo_com_atributos_esperados(self) -> None:
        disciplina: Disciplina = FabricaTesteDisciplina.build()

        modelo_disciplina = ModeloDisciplina.de_entidade(disciplina)

        atributos = [
            modelo_disciplina.id,
            modelo_disciplina.nome,
            modelo_disciplina.carga_horaria,
            modelo_disciplina.ativo
        ]
        esperados = [
            disciplina.id.valor,
            disciplina.nome.valor,
            disciplina.carga_horaria.valor,
            disciplina.ativo
        ]
        self.assertEqual(atributos, esperados)
