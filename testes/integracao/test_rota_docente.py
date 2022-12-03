import json
from uuid import UUID, uuid4
from django.urls import reverse
from rest_framework.test import APITestCase

from testes.fabricas import FabricaTesteModeloDocente, FabricaTesteId
from aplicacao.models import ModeloDocente
from dominio.objetos_de_valor import Id


class TestRotaDocente(APITestCase):
    @staticmethod
    def contruir_url(id_: UUID) -> str:
        return reverse('docente', kwargs={'id_': str(id_)})

    @staticmethod
    def construir_url_aleatoria() -> str:
        id_: Id = FabricaTesteId.build()
        return TestRotaDocente.contruir_url(id_.valor)

    def test_get_QUANDO_id_existe_ENTAO_retorna_status_200(self) -> None:
        modelo_docente: ModeloDocente = FabricaTesteModeloDocente.create()
        url = self.contruir_url(id_=modelo_docente.id)

        response = self.client.get(path=url)

        self.assertEqual(response.status_code, 200)

    def test_get_QUANDO_id_existe_ENTAO_retorna_payload_esperado(self) -> None:
        modelo_docente: ModeloDocente = FabricaTesteModeloDocente.create(ativo=True)
        url = self.contruir_url(id_=modelo_docente.id)

        response = self.client.get(path=url)

        payload_resultante = json.loads(response.content)
        payload_esperado = {
            'id': modelo_docente.id,
            'nome': modelo_docente.nome,
            'ativo': modelo_docente.ativo
        }
        self.assertEqual(payload_resultante, payload_esperado)

    def test_get_QUANDO_id_nao_existe_ENTAO_retorna_status_404(self) -> None:
        url = self.construir_url_aleatoria()

        response = self.client.get(url)

        self.assertEqual(response.status_code, 404)

    def test_post_QUANDO_id_existe_ENTAO_retorna_status_200(self) -> None:
        modelo_docente: ModeloDocente = FabricaTesteModeloDocente.create(ativo=True)
        url = self.contruir_url(id_=modelo_docente.id)
        data = {
            'id': modelo_docente.id,
            'nome': modelo_docente.nome,
            'ativo': modelo_docente.ativo
        }

        response = self.client.post(path=url, data=data)

        self.assertEqual(response.status_code, 200)

    def test_post_QUANDO_id_existe_ENTAO_edita_docente(self) -> None:
        modelo_docente_antes: ModeloDocente = FabricaTesteModeloDocente.create(ativo=True)
        nome_novo = 'Nome Alterado'
        url = self.contruir_url(id_=modelo_docente_antes.id)
        data = {
            'id': modelo_docente_antes.id,
            'nome': nome_novo,
            'ativo': modelo_docente_antes.ativo
        }

        self.client.post(path=url, data=data)

        modelo_docente_depois = ModeloDocente.objects.get(pk=modelo_docente_antes.id)
        self.assertEqual(modelo_docente_depois.nome, nome_novo)

    def test_post_QUANDO_id_nao_existe_ENTAO_retorna_status_404(self) -> None:
        url = self.construir_url_aleatoria()
        data = {
            'id': uuid4(),
            'nome': 'Nome falso',
            'ativo': True
        }

        response = self.client.post(path=url, data=data)

        self.assertEqual(response.status_code, 404)

    def test_post_QUANDO_sucesso_ENTAO_retorna_payload_esperado(self) -> None:
        modelo_docente_antes: ModeloDocente = FabricaTesteModeloDocente.create(ativo=True)
        url = self.contruir_url(id_=modelo_docente_antes.id)
        data = {
            'id': modelo_docente_antes.id,
            'nome': modelo_docente_antes.nome,
            'ativo': modelo_docente_antes.ativo
        }

        response = self.client.post(path=url, data=data)

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


