import json

from django.urls import reverse
from rest_framework.test import APITestCase

from aplicacao.models import ModeloDocente


class TestRotaDocentes(APITestCase):
    def setUp(self) -> None:
        self.url = reverse('docentes')

    def test_post_QUANDO_request_contem_somente_nome_ENTAO_retorna_status_201(self) -> None:
        data = {
            'nome': 'Nome Válido'
        }

        response = self.client.post(path=self.url, data=data, format='json')

        self.assertEqual(response.status_code, 201)

    def test_post_QUANDO_body_vazio_ENTAO_retorna_status_400(self) -> None:
        data = {}

        response = self.client.post(path=self.url, data=data, format='json')

        self.assertEqual(response.status_code, 400)

    def test_post_QUANDO_nome_invalido_ENTAO_retorna_status_400(self) -> None:
        data = {
            'nome': ''
        }

        response = self.client.post(path=self.url, data=data, format='json')

        self.assertEqual(response.status_code, 400)

    def test_post_QUANDO_body_valido_ENTAO_cria_docente_no_banco_de_dados(self) -> None:
        data = {
            'nome': 'Nome Válido'
        }

        response = self.client.post(path=self.url, data=data, format='json')

        conteudo = json.loads(response.content)
        id_do_docente = conteudo['id']
        nome_esperado = data['nome']
        moodelo_docente = ModeloDocente.objects.get(id=id_do_docente)
        self.assertEqual(moodelo_docente.nome, nome_esperado)

    def test_post_QUANDO_body_valido_ENTAO_retorna_json_esperado_com_nome_esperado(self) -> None:
        data = {
            'nome': 'Nome Válido'
        }

        response = self.client.post(path=self.url, data=data, format='json')

        conteudo = json.loads(response.content)
        nome_resultante = conteudo['nome']
        nome_esperado = data['nome']
        self.assertEqual(nome_resultante, nome_esperado)