import json

from django.urls import reverse
from rest_framework.test import APITestCase

from aplicacao.models import ModeloDisciplina
from dominio.otds import OTDDisciplinaEmCriacao
from testes.fabricas import FabricaTesteOTDDisciplinaEmCriacao


class TestRotaDisciplinas(APITestCase):
    def setUp(self) -> None:
        self.url = reverse('disciplinas')

    def test_post_QUANDO_payload_valido_ENTAO_retorna_status_201(self) -> None:
        data = FabricaTesteOTDDisciplinaEmCriacao.build().__dict__

        response = self.client.post(path=self.url, data=data, format='json')

        self.assertEqual(response.status_code, 201)

    def test_post_QUANDO_body_vazio_ENTAO_retorna_status_400(self) -> None:
        data = {}

        response = self.client.post(path=self.url, data=data, format='json')

        self.assertEqual(response.status_code, 400)

    def test_post_QUANDO_body_valido_ENTAO_cria_disciplina_no_banco_de_dados(self) -> None:
        otd_disciplina_em_ciacao: OTDDisciplinaEmCriacao = FabricaTesteOTDDisciplinaEmCriacao.build()
        data = otd_disciplina_em_ciacao.__dict__

        response = self.client.post(path=self.url, data=data, format='json')

        conteudo = json.loads(response.content)
        id_ = conteudo['id']
        ModeloDisciplina.objects.get(id=id_)

    def test_post_QUANDO_disciplina_criada_ENTAO_retorna_payload_com_atributos_esperados(self) -> None:
        otd_disciplina_em_ciacao: OTDDisciplinaEmCriacao = FabricaTesteOTDDisciplinaEmCriacao.build()
        data = otd_disciplina_em_ciacao.__dict__

        response = self.client.post(path=self.url, data=data, format='json')

        conteudo = json.loads(response.content)
        atributos = [
            conteudo['nome'],
            conteudo['carga_horaria']
        ]
        esperado = [
            otd_disciplina_em_ciacao.nome,
            otd_disciplina_em_ciacao.carga_horaria
        ]
        self.assertEqual(atributos, esperado)
