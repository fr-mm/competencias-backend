from typing import List

from django.test import TestCase

from aplicacao.models import ModeloModulo, ModeloDisciplina, ModeloDisciplinaEmModulo
from aplicacao.repositorios import RepositorioModulo
from dominio.entidades import Modulo
from dominio.objetos_de_valor import Id
from testes.fabricas import FabricaTesteModulo, FabricaTesteModeloDisciplina, FabricaTesteModeloModulo


class TestRepositorioModulo(TestCase):
    def setUp(self) -> None:
        self.repositorio = RepositorioModulo()

    def test_salvar_QUANDO_modulo_sem_disciplinas_ENTAO_salva_modulo_no_banco_de_dados(self) -> None:
        modulo: Modulo = FabricaTesteModulo.build(disciplinas_ids=[])

        self.repositorio.salvar(modulo)

        ModeloModulo.objects.get(pk=modulo.id.valor)

    def test_salvar_QUANDO_modulo_com_disciplinas_ENTAO_atualiza_disciplinas_no_banco_de_dados(self) -> None:
        modelo_disciplina_existente: ModeloDisciplina = FabricaTesteModeloDisciplina.create()
        modelo_disciplina_a_ser_deletada: ModeloDisciplina = FabricaTesteModeloDisciplina.create()
        modelo_disciplina_nova: ModeloDisciplina = FabricaTesteModeloDisciplina.create()
        modelo_modulo: ModeloModulo = FabricaTesteModeloModulo.create()
        ModeloDisciplinaEmModulo(disciplina=modelo_disciplina_existente, modulo=modelo_modulo).save()
        ModeloDisciplinaEmModulo(disciplina=modelo_disciplina_a_ser_deletada, modulo=modelo_modulo).save()
        modulo: Modulo = FabricaTesteModulo.build(
            id_=Id(modelo_modulo.id),
            disciplinas_ids=[
                Id(modelo_disciplina_existente.id),
                Id(modelo_disciplina_nova.id)
            ]
        )

        self.repositorio.salvar(modulo)

        disciplinas_no_modulo: List[ModeloDisciplinaEmModulo] = ModeloDisciplinaEmModulo.objects.filter(modulo=modelo_modulo)
        ids_disciplinas_no_modulo = [disciplina_no_modulo.disciplina.id for disciplina_no_modulo in disciplinas_no_modulo]
        ids_esperadas = [modelo_disciplina_existente.id, modelo_disciplina_nova.id]
        self.assertEqual(ids_disciplinas_no_modulo, ids_esperadas)

