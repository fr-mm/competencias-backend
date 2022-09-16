import json
from typing import Dict

from django.test import TestCase
from django.urls import reverse

from aplicacao.models import ModeloUsuario
from aplicacao.serializers import SerializerCadastroUsuario
from testes.fabricas import FabricaTesteNomeDeUsuario, FabricaTesteEmail


class TestRotaLogin(TestCase):
    def setUp(self) -> None:
        self.url = reverse('login')
        self.payload_valido = {
            'nome': FabricaTesteNomeDeUsuario.build().valor,
            'email': FabricaTesteEmail.build().valor,
            'password': 'fake_password123'
        }

    @staticmethod
    def cadastrar_usuario(paylad: Dict[str, str]) -> ModeloUsuario:
        serializer = SerializerCadastroUsuario(data=paylad)
        serializer.is_valid(raise_exception=True)
        return serializer.save()

    def test_post_QUANDO_usuario_existe_ENTAO_retorna_status_200(self) -> None:
        self.cadastrar_usuario(self.payload_valido)

        response = self.client.post(path=self.url, data=self.payload_valido, format='json')

        self.assertEqual(response.status_code, 200)

    def test_post_QUANDO_usuario_existe_ENTAO_retorna_token_com_comprimento_esperado(self) -> None:
        self.cadastrar_usuario(self.payload_valido)

        response = self.client.post(path=self.url, data=self.payload_valido, format='json')

        comprimento_esperado = 64
        token = json.loads(response.content)['token']
        self.assertEqual(len(token), comprimento_esperado)

    def test_post_QUANDO_usuario_existe_ENTAO_loga_client(self) -> None:
        self.cadastrar_usuario(self.payload_valido)

        logou = self.client.login(email=self.payload_valido['email'], password=self.payload_valido['password'])

        self.assertTrue(logou)

    def test_post_QUANDO_password_errada_ENTAO_nao_loga_client(self) -> None:
        self.cadastrar_usuario(self.payload_valido)
        passoword_errada = 'wrongpsss432*'

        logou = self.client.login(email=self.payload_valido['email'], password=passoword_errada)

        self.assertFalse(logou)
