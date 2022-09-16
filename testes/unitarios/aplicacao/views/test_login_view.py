from typing import Dict
from urllib.request import Request

from django.test import TestCase

from aplicacao.models import ModeloUsuario
from aplicacao.serializers import SerializerCadastroUsuario
from aplicacao.views import LoginView
from testes.fabricas import FabricaTesteEmail, FabricaTesteNomeDeUsuario


class TestLoginView(TestCase):
    def setUp(self) -> None:
        self.url = f'https://localhost:8000'
        self.payload_valido = {
            'nome': FabricaTesteNomeDeUsuario.build().valor,
            'email': FabricaTesteEmail.build().valor,
            'password': 'fake_password123'
        }
        self.login_view = LoginView()

    @staticmethod
    def cadastrar_usuario(paylad: Dict[str, str]) -> ModeloUsuario:
        serializer = SerializerCadastroUsuario(data=paylad)
        serializer.is_valid(raise_exception=True)
        return serializer.save()

    def test_post_QUANDO_payload_valido_ENTAO_retorna_status_code_200(self):
        self.cadastrar_usuario(self.payload_valido)
        request = Request(self.url, data=self.payload_valido)

        response = self.login_view.post(request)

        self.assertEqual(response.status_code, 200)

    def test_post_QUANDO_payload_valido_ENTAO_retorna_response_com_usuario_serializado_com_atributos_esperados(self):
        self.cadastrar_usuario(self.payload_valido)
        request = Request(self.url, data=self.payload_valido)

        response = self.login_view.post(request)

        usuario = response.data['usuario']
        atributos_resultantes = [
            usuario['nome'],
            usuario['email']
        ]
        atributos_esperados = [
            self.payload_valido['nome'],
            self.payload_valido['email']
        ]
        self.assertEqual(atributos_resultantes, atributos_esperados)

    def test_post_QUANDO_payload_valida_ENTAO_retorna_token_com_comprimento_esperado(self) -> None:
        self.cadastrar_usuario(self.payload_valido)
        request = Request(self.url, data=self.payload_valido)

        response = self.login_view.post(request)

        token = response.data['token']
        comprimento_esperado = 64
        self.assertEqual(len(token), comprimento_esperado)

    def test_post_QUANDO_senha_errada_ENTAO_retorna_status_400(self) -> None:
        payload_invalido = self.payload_valido
        payload_invalido['password'] = '123456'
        request = Request(self.url, data=payload_invalido)

        response = self.login_view.post(request)

        self.assertEqual(response.status_code, 400)
