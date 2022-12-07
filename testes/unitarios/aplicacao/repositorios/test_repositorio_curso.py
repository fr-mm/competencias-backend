from typing import List

from django.test import TestCase

from aplicacao.models import ModeloModulo, ModeloCurso, ModeloModuloEmCurso
from aplicacao.repositorios import RepositorioCurso
from dominio.entidades import Curso
from dominio.objetos_de_valor import Id
from testes.fabricas import FabricaTesteModeloModulo, \
    FabricaTesteCurso, FabricaTesteModeloCurso


class TestRepositorioCurso(TestCase):
    def setUp(self) -> None:
        self.repositorio = RepositorioCurso()

    def test_salvar_QUANDO_curso_sem_modulos_ENTAO_salva_curso_no_banco_de_dados(self) -> None:
        curso: Curso = FabricaTesteCurso.build(modulos_ids=[])

        self.repositorio.salvar(curso)

        ModeloCurso.objects.get(pk=curso.id.valor)

    def test_salvar_QUANDO_curso_com_modulos_ENTAO_atualiza_modulos_no_banco_de_dados(self) -> None:
        modelo_modulo_existente: ModeloModulo = FabricaTesteModeloModulo.create()
        modelo_modulo_a_ser_deletado: ModeloModulo = FabricaTesteModeloModulo.create()
        modelo_modulo_novo: ModeloModulo = FabricaTesteModeloModulo.create()
        modelo_curso: ModeloCurso = FabricaTesteModeloCurso.create()
        ModeloModuloEmCurso(curso=modelo_curso, modulo=modelo_modulo_existente).save()
        ModeloModuloEmCurso(curso=modelo_curso, modulo=modelo_modulo_a_ser_deletado).save()
        curso: Curso = FabricaTesteCurso.build(
            id_=Id(modelo_curso.id),
            modulos_ids=[
                Id(modelo_modulo_existente.id),
                Id(modelo_modulo_novo.id)
            ]
        )

        self.repositorio.salvar(curso)

        modulos_no_curso: List[ModeloModuloEmCurso] = ModeloModuloEmCurso.objects.filter(curso=modelo_curso)
        ids_modulos_no_curso = [modulos_no_curso.modulo.id for modulos_no_curso in modulos_no_curso]
        ids_esperadas = [modelo_modulo_existente.id, modelo_modulo_novo.id]
        self.assertEqual(ids_modulos_no_curso, ids_esperadas)
