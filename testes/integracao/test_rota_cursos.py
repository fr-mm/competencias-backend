import json
from typing import Dict

from django.urls import reverse
from rest_framework.test import APITestCase

from aplicacao.models import ModeloCurso, ModeloModulo, ModeloModuloEmCurso, ModeloDisciplinaEmModulo, ModeloDisciplina
from dominio.otds import OTDCursoEmCriacao, OTDModuloEmCriacao
from testes.fabricas import FabricaTesteOTDCursoEmCriacao, FabricaTesteModeloDisciplina


class TestRotaCurso(APITestCase):
    def setUp(self) -> None:
        self.url = reverse('cursos')

    @staticmethod
    def otd_para_request_data(otd: OTDCursoEmCriacao) -> Dict[str, any]:
        modulos = []
        for otd_modulo in otd.modulos:
            modulo = otd_modulo.__dict__
            modulo['disciplinas_ids'] = [str(id_) for id_ in modulo['disciplinas_ids']]
            modulos.append(modulo)

        return {
            'nome': otd.nome,
            'modulos': modulos,
        }

    def test_post_QUANDO_criado_ENTAO_retorna_status_201(self) -> None:
        otd_entrada = FabricaTesteOTDCursoEmCriacao.build(modulos=[])

        request_data = self.otd_para_request_data(otd_entrada)

        response = self.client.post(
            path=self.url,
            data=json.dumps(request_data),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, 201)

    def test_post_QUANDO_criado_ENTAO_altera_banco_de_dados(self) -> None:
        modelo_disciplina: ModeloDisciplina = FabricaTesteModeloDisciplina.create()
        numero_modulo = 1
        otd_entrada: OTDCursoEmCriacao = FabricaTesteOTDCursoEmCriacao.build(modulos=[
            OTDModuloEmCriacao(numero=numero_modulo, disciplinas_ids=[modelo_disciplina.id])
        ])

        request_data = self.otd_para_request_data(otd_entrada)

        self.client.post(
            path=self.url,
            data=json.dumps(request_data),
            content_type='application/json'
        )

        modelo_curso = ModeloCurso.objects.all()[0]
        modelo_modulo = ModeloModulo.objects.all()[0]
        modulo_em_curso = ModeloModuloEmCurso.objects.all()[0]
        disciplina_em_modulo = ModeloDisciplinaEmModulo.objects.all()[0]
        resultdo = {
            'nome_curso': modelo_curso.nome,
            'numero_modulo': modelo_modulo.numero,
            'modulo_em_curso': {
                'numero_modulo': modulo_em_curso.modulo.numero,
                'nome_curso': modulo_em_curso.curso.nome
            },
            'disciplina_em_modulo': {
                'numero_modulo': disciplina_em_modulo.modulo.numero,
                'nome_disciplina': disciplina_em_modulo.disciplina.nome
            }

        }
        esperado = {
            'nome_curso': otd_entrada.nome,
            'numero_modulo': numero_modulo,
            'modulo_em_curso': {
                'numero_modulo': numero_modulo,
                'nome_curso': otd_entrada.nome
            },
            'disciplina_em_modulo': {
                'numero_modulo': numero_modulo,
                'nome_disciplina': modelo_disciplina.nome
            }

        }
        self.assertEqual(resultdo, esperado)
