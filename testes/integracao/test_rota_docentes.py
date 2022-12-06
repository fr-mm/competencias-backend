import json
from typing import Dict

from django.urls import reverse
from rest_framework.test import APITestCase

from dominio.entidades import Docente
from testes.fabricas import FabricaTesteModeloDocente, FabricaTesteDocente, FabricaTesteModeloUnidadeSenai
from aplicacao.models import ModeloDocente


class TestRotaDocentes(APITestCase):
    def setUp(self) -> None:
        self.url = reverse('docentes')

    @staticmethod
    def criar_request_data(nome: str = None) -> Dict[str, any]:
        docente: Docente = FabricaTesteDocente.build()
        FabricaTesteModeloUnidadeSenai.create(id=docente.unidade_senai_id.valor)
        return {
            'id': str(docente.id.valor),
            'nome': nome or docente.nome.valor,
            'email': docente.email.valor,
            'telefones': [telefone.valor for telefone in docente.telefones],
            'tipo_de_contratacao': docente.tipo_de_contratacao.valor.value,
            'unidade_senai_id': str(docente.unidade_senai_id.valor),
            'ativo': docente.ativo
        }

    def test_post_QUANDO_payload_valido_ENTAO_retorna_status_201(self) -> None:
        data = self.criar_request_data()

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
        data = self.criar_request_data()

        response = self.client.post(path=self.url, data=data, format='json')

        conteudo = json.loads(response.content)
        id_do_docente = conteudo['id']
        nome_esperado = data['nome']
        moodelo_docente = ModeloDocente.objects.get(id=id_do_docente)
        self.assertEqual(moodelo_docente.nome, nome_esperado)

    def test_post_QUANDO_body_valido_ENTAO_retorna_json_esperado_com_nome_esperado(self) -> None:
        data = self.criar_request_data()

        response = self.client.post(path=self.url, data=data, format='json')

        conteudo = json.loads(response.content)
        nome_resultante = conteudo['nome']
        nome_esperado = data['nome']
        self.assertEqual(nome_resultante, nome_esperado)

    def test_get_QUANDO_chamado_ENTAO_retorna_status_200(self) -> None:
        response = self.client.get(path=self.url)

        self.assertEqual(response.status_code, 200)

    def test_get_QUANDO_docentes_existem_ENTAO_retorna_json_esperado(self) -> None:
        modelo_unidade_senai = FabricaTesteModeloUnidadeSenai.create()
        modelos: [ModeloDocente] = [FabricaTesteModeloDocente.create(
            ativo=True,
            unidade_senai=modelo_unidade_senai
        ) for _ in range(2)]
        FabricaTesteModeloDocente.create(ativo=False)

        response = self.client.get(path=self.url)

        json_resultante = json.loads(response.content)
        json_esperado = [
            {
                'id': str(modelo.id),
                'nome': modelo.nome,
                'email': modelo.email,
                'telefones': [],
                'tipo_de_contratacao': modelo.tipo_de_contratacao,
                'unidade_senai_id': str(modelo_unidade_senai.id),
                'ativo': modelo.ativo
            } for modelo in modelos
        ]
        self.assertEqual(json_resultante, json_esperado)
