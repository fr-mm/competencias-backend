import json
from typing import Dict
from uuid import UUID, uuid4

from django.urls import reverse
from rest_framework.test import APITestCase

from aplicacao.models import ModeloDisciplina
from dominio.objetos_de_valor import Id
from testes.fabricas import FabricaTesteId, FabricaTesteModeloDisciplina


class TestRotaDisciplina(APITestCase):
    @staticmethod
    def contruir_url(id_: UUID) -> str:
        return reverse('disciplina', kwargs={'id_': str(id_)})

    @staticmethod
    def construir_url_aleatoria() -> str:
        id_: Id = FabricaTesteId.build()
        return TestRotaDisciplina.contruir_url(id_.valor)

    @staticmethod
    def modelo_para_request_data(modelo: ModeloDisciplina) -> Dict[str, any]:
        return {
            'id': str(modelo.id),
            'nome': modelo.nome,
            'carga_horaria': modelo.carga_horaria,
            'ativo': modelo.ativo
        }

    def test_post_QUANDO_id_existe_ENTAO_retorna_status_200(self) -> None:
        modelo: ModeloDisciplina = FabricaTesteModeloDisciplina.create(ativo=True)
        url = self.contruir_url(id_=modelo.id)
        data = self.modelo_para_request_data(modelo)

        response = self.client.post(path=url, data=json.dumps(data), content_type='application/json')

        self.assertEqual(response.status_code, 200)

    def test_post_QUANDO_id_existe_ENTAO_edita_disciplina(self) -> None:
        modelo_antes: ModeloDisciplina = FabricaTesteModeloDisciplina.create(ativo=True)
        nome_novo = 'Nome Alterado'
        data = self.modelo_para_request_data(modelo_antes)
        data['nome'] = nome_novo

        url = self.contruir_url(id_=modelo_antes.id)

        self.client.post(path=url, data=json.dumps(data), content_type='application/json')

        modelo_depois = ModeloDisciplina.objects.get(pk=modelo_antes.id)
        self.assertEqual(modelo_depois.nome, nome_novo)

    def test_post_QUANDO_id_nao_existe_ENTAO_retorna_status_404(self) -> None:
        url = self.construir_url_aleatoria()
        data = {
            'id': str(uuid4()),
            'nome': 'Foobar',
            'carga_horaria': 8,
            'ativo': True
        }

        response = self.client.post(path=url, data=json.dumps(data), content_type='application/json')

        self.assertEqual(response.status_code, 404)

    def test_post_QUANDO_sucesso_ENTAO_retorna_payload_esperado(self) -> None:
        modelo_antes: ModeloDisciplina = FabricaTesteModeloDisciplina.create(ativo=True)
        url = self.contruir_url(id_=modelo_antes.id)
        data = self.modelo_para_request_data(modelo_antes)

        response = self.client.post(path=url, data=json.dumps(data), content_type='application/json')

        payload_esperado = data
        payload_esperado['id'] = str(payload_esperado['id'])
        self.assertEqual(response.data, payload_esperado)
