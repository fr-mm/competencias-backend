import json
from dataclasses import dataclass
from typing import Dict, List

from django.urls import reverse
from rest_framework.test import APITestCase

from aplicacao.models import ModeloDocente, ModeloDisciplina, ModeloCompetencia
from dominio.otds import OTDCasoDeUsoEditarCompetencias
from testes.fabricas import FabricaTesteModeloDocente, FabricaTesteModeloDisciplina, \
    FabricaTesteOTDCasoDeUsoEditarCompetencias, FabricaTesteOTDCompetencia, FabricaTesteModeloCompetencia


class TestRotaCompetencias(APITestCase):
    def setUp(self) -> None:
        self.url = reverse('competencias')

    @staticmethod
    def otd_para_request_data(otd: OTDCasoDeUsoEditarCompetencias) -> Dict[str, str or int]:
        competencias = []
        for competencia in otd.competencias:
            competencias.append({
                'docente_id': str(competencia.docente_id),
                'disciplina_id': str(competencia.disciplina_id),
                'nivel': competencia.nivel
            })
        return {
            'docente_id': str(otd.docente_id),
            'competencias': competencias
        }

    def test_post_QUANDO_request_data_valido_ENTAO_retorna_status_200(self) -> None:
        docente: ModeloDocente = FabricaTesteModeloDocente.create()
        disciplinas: List[ModeloDisciplina] = [FabricaTesteModeloDisciplina.create() for _ in range(2)]
        otd: OTDCasoDeUsoEditarCompetencias = FabricaTesteOTDCasoDeUsoEditarCompetencias.build(
            docente_id=docente.id,
            competencias=[
                FabricaTesteOTDCompetencia.build(
                    docente_id=docente.id,
                    disciplina_id=disciplina.id
                ) for disciplina in disciplinas
            ]
        )
        request_data = self.otd_para_request_data(otd)

        response = self.client.post(
            path=self.url,
            data=json.dumps(request_data),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, 200)

    def test_post_QUANDO_request_data_valido_ENTAO_altera_competencias(self) -> None:
        docente: ModeloDocente = FabricaTesteModeloDocente.create()
        disciplinas: List[ModeloDisciplina] = [FabricaTesteModeloDisciplina.create() for _ in range(2)]
        otd: OTDCasoDeUsoEditarCompetencias = FabricaTesteOTDCasoDeUsoEditarCompetencias.build(
            docente_id=docente.id,
            competencias=[
                FabricaTesteOTDCompetencia.build(
                    docente_id=docente.id,
                    disciplina_id=disciplina.id
                ) for disciplina in disciplinas
            ]
        )
        request_data = self.otd_para_request_data(otd)

        self.client.post(
            path=self.url,
            data=json.dumps(request_data),
            content_type='application/json'
        )

        competencias: List[ModeloCompetencia] = ModeloCompetencia.objects.all()
        resultado = [{
            'docente': competencia.docente,
            'disciplina': competencia.disciplina,
            'nivel': competencia.nivel
        } for competencia in competencias]
        esperado = [{
            'docente': docente,
            'disciplina': disciplinas[i],
            'nivel': otd.competencias[i].nivel
        } for i in range(2)]
        self.assertEqual(resultado, esperado)
