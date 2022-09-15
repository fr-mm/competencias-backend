import json

from django.urls import reverse
from rest_framework.test import APITestCase

from aplicacao.models import ModeloUsuario
from testes.fabricas import FabricaTesteEmail


class TestRotaUsuarios(APITestCase):
    def setUp(self) -> None:
        self.url = reverse('usuarios')
        self.payload_valido = {
            'nome': 'usuario teste',
            'email': FabricaTesteEmail.build().valor,
            'password': '123456'
        }

    def test_post_QUANDO_payload_valido_ENTAO_returna_status_200(self) -> None:
        response = self.client.post(
            path=self.url,
            data=self.payload_valido
        )

        self.assertEqual(response.status_code, 200)

    def test_post_QUANDO_payload_valido_ENTAO_cria_usuario(self) -> None:
        self.client.post(
            path=self.url,
            data=self.payload_valido
        )

        ModeloUsuario.objects.get(nome=self.payload_valido['nome'])

    def test_post_QUANDO_payload_valido_ENTAO_retorna_dados_do_usuario_criado(self) -> None:
        response = self.client.post(
            path=self.url,
            data=self.payload_valido
        )

        conteudo = json.loads(response.content)
        usuario = conteudo['usuario']
        dados_resultantes = [
            usuario['nome'],
            usuario['email']
        ]
        dados_esperados = [
            self.payload_valido['nome'],
            self.payload_valido['email']
        ]
        self.assertEqual(dados_resultantes, dados_esperados)

    def test_post_QUANDO_payload_valido_ENTATO_retorna_token(self) -> None:
        response = self.client.post(
            path=self.url,
            data=self.payload_valido
        )

        conteudo = json.loads(response.content)
        token = conteudo['token']
        self.assertEqual(len(token), 64)

    def test_post_QUANDO_payload_invalido_ENTAO_retorna_status_400(self) -> None:
        response = self.client.post(
            path=self.url,
            data={}
        )

        self.assertEqual(response.status_code, 400)
