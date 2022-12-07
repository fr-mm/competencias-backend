from django.test import TestCase

from aplicacao.models import ModeloModulo, ModeloCurso
from aplicacao.servicos import ServicoConverterModeloCurso
from dominio.entidades import Curso
from testes.fabricas import FabricaTesteModeloModulo, FabricaTesteCurso, FabricaTesteModeloCurso, \
    FabricaTesteModeloModuloEmCurso


class TestServicoConverterModeloCurso(TestCase):
    def test_de_entidade_QUANDO_entidade_fornecida_ENTAO_retorna_modelo_com_atributos_esperados(self) -> None:
        curso: Curso = FabricaTesteCurso.build(modulos_ids=[])

        modelo_curso = ServicoConverterModeloCurso.de_entidade(curso)

        atributos_resultantes = [
            modelo_curso.id,
            modelo_curso.nome,
            modelo_curso.ativo
        ]
        atributos_esperados = [
            curso.id.valor,
            curso.nome.valor,
            curso.ativo
        ]
        self.assertEqual(atributos_resultantes, atributos_esperados)

    def test_para_entidade_QUANDO_modelo_fornecido_ENTAO_retorna_entidade_com_atributos_esperados(self) -> None:
        modelo_curso: ModeloCurso = FabricaTesteModeloCurso.create()
        modelo_modulo: ModeloModulo = FabricaTesteModeloModulo.create()
        FabricaTesteModeloModuloEmCurso.create(modulo=modelo_modulo, curso=modelo_curso)

        curso = ServicoConverterModeloCurso.para_entidade(modelo_curso)

        atributos_resultantes = [
            curso.id.valor,
            curso.nome.valor,
            [modulo_id.valor for modulo_id in curso.modulos_ids],
            curso.ativo
        ]
        atributos_esperados = [
            modelo_curso.id,
            modelo_curso.nome,
            [modelo_modulo.id],
            modelo_curso.ativo
        ]
        self.assertEqual(atributos_resultantes, atributos_esperados)
