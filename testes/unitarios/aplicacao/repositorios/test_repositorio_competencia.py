from typing import List

from django.test import TestCase

from aplicacao.models import ModeloCompetencia, ModeloDocente, ModeloDisciplina
from aplicacao.repositorios import RepositorioCompetencia
from dominio.entidades import Competencia
from dominio.enums import NivelDeCompetenciaEnum
from dominio.objetos_de_valor import Id
from testes.fabricas import FabricaTesteCompetencia, FabricaTesteModeloDocente, FabricaTesteModeloDisciplina, \
    FabricaTesteModeloCompetencia


class TestRepositorioCompetencia(TestCase):
    def setUp(self) -> None:
        self.repositorio = RepositorioCompetencia()

    def test_salvar_QUANDO_competencias_informadas_ENTAO_salva_no_banco_de_dados(self) -> None:
        docente: ModeloDocente = FabricaTesteModeloDocente.create()
        disciplinas: List[ModeloDisciplina] = [FabricaTesteModeloDisciplina.create() for _ in range(2)]
        competencias: List[Competencia] = [
            FabricaTesteCompetencia.build(
                docente_id=Id(docente.id),
                disciplina_id=Id(disciplina.id)
            ) for disciplina in disciplinas
        ]

        self.repositorio.salvar(competencias[0], competencias[1])

        modelos: List[ModeloCompetencia] = ModeloCompetencia.objects.all()
        resultado = {
            f'modelo{i}': {
                'docente': modelos[i].docente.id,
                'disciplina': modelos[i].disciplina.id,
                'nivel': modelos[i].nivel
            } for i in range(2)
        }
        esperado = {
            f'modelo{i}': {
                'docente': competencias[i].docente_id.valor,
                'disciplina': competencias[i].disciplina_id.valor,
                'nivel': competencias[i].nivel.value
            } for i in range(2)
        }
        print(resultado)
        print(esperado)
        self.assertEqual(resultado, esperado)

    def test_trazer_por_id_de_docente_QUANDO_id_informada_ENTAO_traz_competencias_do_docente(self) -> None:
        docente_alvo: ModeloDocente = FabricaTesteModeloDocente.create()
        outro_docente: ModeloDocente = FabricaTesteModeloDocente.create()
        disciplinas: List[ModeloDisciplina] = [FabricaTesteModeloDisciplina.create() for _ in range(3)]
        competencias_do_docente_alvo: List[ModeloCompetencia] = [
            FabricaTesteModeloCompetencia.create(
                docente=docente_alvo,
                disciplina=disciplinas[i]
            ) for i in range(2)
        ]
        FabricaTesteModeloCompetencia.create(
            docente=outro_docente,
            disciplina=disciplinas[2]
        )

        resultado = self.repositorio.trazer_id_de_docente(Id(docente_alvo.id))

        esperado = [
            Competencia(
                docente_id=Id(docente_alvo.id),
                disciplina_id=Id(competencia.disciplina.id),
                nivel=NivelDeCompetenciaEnum(competencia.nivel)
            ) for competencia in competencias_do_docente_alvo
        ]
        print(resultado)
        print(esperado)
        self.assertEqual(resultado, esperado)

    def test_deletar_todos_de_docente_QUANDO_id_informado_ENTAO_deleta_competencias_do_banco_de_dados(self) -> None:
        docente_alvo: ModeloDocente = FabricaTesteModeloDocente.create()
        disciplinas: List[ModeloDisciplina] = [FabricaTesteModeloDisciplina.create() for _ in range(2)]
        [
            FabricaTesteModeloCompetencia.create(
                docente=docente_alvo,
                disciplina=disciplinas[i]
            ) for i in range(2)
        ]

        self.repositorio.deletar_todos_de_docente(Id(docente_alvo.id))

        competencias_no_banco_de_dados = ModeloCompetencia.objects.all()
        self.assertEqual(len(competencias_no_banco_de_dados), 0)
