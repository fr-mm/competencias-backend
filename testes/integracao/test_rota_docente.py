import json
from typing import Dict
from uuid import UUID, uuid4
from django.urls import reverse
from rest_framework.test import APITestCase

from aplicacao.serializers import SerializerOTDDocente
from testes.fabricas import FabricaTesteModeloDocente, FabricaTesteId, FabricaTesteModeloTelefone, \
    FabricaTesteTipoDeContratacao
from aplicacao.models import ModeloDocente, ModeloTelefone
from dominio.objetos_de_valor import Id


class TestRotaDocente(APITestCase):
    def setUp(self) -> None:
        self.telefones = []

    @staticmethod
    def contruir_url(id_: UUID) -> str:
        return reverse('docente', kwargs={'id_': str(id_)})

    @staticmethod
    def construir_url_aleatoria() -> str:
        id_: Id = FabricaTesteId.build()
        return TestRotaDocente.contruir_url(id_.valor)

    def modelo_docente_para_request_data(self, modelo_docente: ModeloDocente) -> Dict[str, any]:
        return {
            'id': str(modelo_docente.id),
            'nome': modelo_docente.nome,
            'email': modelo_docente.email,
            'telefones': [telefone.numero for telefone in self.telefones],
            'tipo_de_contratacao': modelo_docente.tipo_de_contratacao,
            'unidade_senai_id': str(modelo_docente.unidade_senai.id),
            'ativo': modelo_docente.ativo
        }

    def test_get_QUANDO_id_existe_ENTAO_retorna_status_200(self) -> None:
        modelo_docente: ModeloDocente = FabricaTesteModeloDocente.create()
        url = self.contruir_url(id_=modelo_docente.id)

        response = self.client.get(path=url)

        self.assertEqual(response.status_code, 200)

    def test_get_QUANDO_id_existe_ENTAO_retorna_payload_esperado(self) -> None:
        modelo_docente: ModeloDocente = FabricaTesteModeloDocente.create(ativo=True)
        self.telefones = [FabricaTesteModeloTelefone.create(docente=modelo_docente)]
        url = self.contruir_url(id_=modelo_docente.id)

        response = self.client.get(path=url)

        payload_resultante = json.loads(response.content)
        payload_esperado = self.modelo_docente_para_request_data(modelo_docente)
        self.assertEqual(payload_resultante, payload_esperado)

    def test_get_QUANDO_id_nao_existe_ENTAO_retorna_status_404(self) -> None:
        url = self.construir_url_aleatoria()

        response = self.client.get(url)

        self.assertEqual(response.status_code, 404)

    def test_post_QUANDO_id_existe_ENTAO_retorna_status_200(self) -> None:
        modelo_docente: ModeloDocente = FabricaTesteModeloDocente.create(ativo=True)
        url = self.contruir_url(id_=modelo_docente.id)
        data = self.modelo_docente_para_request_data(modelo_docente)

        response = self.client.post(path=url, data=json.dumps(data), content_type='application/json')

        self.assertEqual(response.status_code, 200)

    def test_post_QUANDO_id_existe_ENTAO_edita_docente(self) -> None:
        modelo_docente_antes: ModeloDocente = FabricaTesteModeloDocente.create(ativo=True)

        nome_novo = 'Nome Alterado'
        data = self.modelo_docente_para_request_data(modelo_docente_antes)
        data['nome'] = nome_novo

        url = self.contruir_url(id_=modelo_docente_antes.id)

        self.client.post(path=url, data=json.dumps(data), content_type='application/json')

        modelo_docente_depois = ModeloDocente.objects.get(pk=modelo_docente_antes.id)
        self.assertEqual(modelo_docente_depois.nome, nome_novo)

    def test_post_QUANDO_id_nao_existe_ENTAO_retorna_status_404(self) -> None:
        url = self.construir_url_aleatoria()
        data = {
            'id': str(uuid4()),
            'nome': 'Foobar',
            'email': 'email@emeail.com',
            'telefones': ['(00)0000-0000'],
            'tipo_de_contratacao': FabricaTesteTipoDeContratacao.build().valor.value,
            'unidade_senai_id': str(uuid4()),
            'ativo': True
        }

        response = self.client.post(path=url, data=json.dumps(data), content_type='application/json')

        self.assertEqual(response.status_code, 404)

    def test_post_QUANDO_sucesso_ENTAO_retorna_payload_esperado(self) -> None:
        modelo_docente_antes: ModeloDocente = FabricaTesteModeloDocente.create(ativo=True)
        url = self.contruir_url(id_=modelo_docente_antes.id)
        data = self.modelo_docente_para_request_data(modelo_docente_antes)

        response = self.client.post(path=url, data=json.dumps(data), content_type='application/json')

        payload_esperado = data
        payload_esperado['id'] = str(payload_esperado['id'])
        self.assertEqual(response.data, payload_esperado)

    def test_delete_QUANDO_id_existe_ENTAO_retorna_status_200(self) -> None:
        modelo_docente: ModeloDocente = FabricaTesteModeloDocente.create(ativo=True)
        url = self.contruir_url(id_=modelo_docente.id)

        response = self.client.delete(path=url)

        self.assertEqual(response.status_code, 200)

    def test_delete_QUANDO_id_existe_ENTAO_desativa_docente(self) -> None:
        modelo_docente_antes: ModeloDocente = FabricaTesteModeloDocente.create(ativo=True)
        url = self.contruir_url(id_=modelo_docente_antes.id)

        self.client.delete(path=url)

        modelo_docente_depois = ModeloDocente.objects.get(pk=modelo_docente_antes.id)
        self.assertFalse(modelo_docente_depois.ativo)

    def test_delete_QUANDO_id_nao_existe_ENTAO_retorna_status_404(self) -> None:
        url = self.construir_url_aleatoria()

        response = self.client.delete(path=url)

        self.assertEqual(response.status_code, 404)


