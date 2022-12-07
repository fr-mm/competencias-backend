from django.test import TestCase

from aplicacao.models import ModeloDisciplina, ModeloModulo
from aplicacao.servicos import ServicoConverterModeloModulo
from dominio.entidades import Modulo
from testes.fabricas import FabricaTesteModulo, FabricaTesteModeloDisciplina, FabricaTesteModeloModulo, \
    FabricaTesteModeloDisciplinaEmModulo


class TestServicoConverterModeloModulo(TestCase):
    def test_de_entidade_QUANDO_entidade_fornecida_ENTAO_retorna_modelo_com_atributos_esperados(self) -> None:
        modulo: Modulo = FabricaTesteModulo.build(disciplinas_ids=[])

        modelo_modulo = ServicoConverterModeloModulo.de_entidade(modulo)

        atributos_resultantes = [
            modelo_modulo.id,
            modelo_modulo.numero
        ]
        atributos_esperados = [
            modulo.id.valor,
            modulo.numero.valor
        ]
        self.assertEqual(atributos_resultantes, atributos_esperados)

    def test_para_entidade_QUANDO_modelo_fornecido_ENTAO_retorna_entidade_com_atributos_esperados(self) -> None:
        modelo_modulo: ModeloModulo = FabricaTesteModeloModulo.create()
        modelo_disciplina: ModeloDisciplina = FabricaTesteModeloDisciplina.create()
        FabricaTesteModeloDisciplinaEmModulo.create(modulo=modelo_modulo, disciplina=modelo_disciplina)

        modulo = ServicoConverterModeloModulo.para_entidade(modelo_modulo)

        atributos_resultantes = [
            modulo.id.valor,
            modulo.numero.valor,
            [disciplina_id.valor for disciplina_id in modulo.disciplinas_ids],
        ]
        atributos_esperados = [
            modelo_modulo.id,
            modelo_modulo.numero,
            [modelo_disciplina.id],
        ]
        self.assertEqual(atributos_resultantes, atributos_esperados)
