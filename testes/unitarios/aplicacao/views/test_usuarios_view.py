from urllib.request import Request

from django.test import TestCase

from aplicacao.views import UsuariosView
from testes.fabricas import FabricaTesteNomeDeUsuario, FabricaTesteEmail


class TestUsuariosView(TestCase):
    def setUp(self) -> None:
        self.url = f'https://localhost:8000'
        self.payload_valido = {
            'nome': FabricaTesteNomeDeUsuario.build().valor,
            'email': FabricaTesteEmail.build().valor,
            'password': '12*3f89&sdf4@fu5SF'
        }
        self.usuarios_view = UsuariosView()

    def test_post_QUANDOD_payload_valido_ENTAO_retorna_status_201(self) -> None:
        request = Request(self.url, data=self.payload_valido)

        response = self.usuarios_view.post(request)

        self.assertEqual(response.status_code, 201)

    def test_post_QUANDO_payload_valido_ENTAO_retorna_response_com_usuario_serializado_com_atributos_esperados(self):
        request = Request(self.url, data=self.payload_valido)

        response = self.usuarios_view.post(request)

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
        request = Request(self.url, data=self.payload_valido)

        response = self.usuarios_view.post(request)

        token = response.data['token']
        comprimento_esperado = 64
        self.assertEqual(len(token), comprimento_esperado)

    def test_post_QUANDO_payload_invalido_ENTAO_retorna_status_400(self) -> None:
        request = Request(self.url, data={})

        response = self.usuarios_view.post(request)

        self.assertEqual(response.status_code, 400)
