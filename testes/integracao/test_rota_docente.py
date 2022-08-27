import json
from uuid import UUID

from django.urls import reverse
from rest_framework.test import APITestCase

from aplicacao.models import ModeloDocente
from dominio.objetos_de_valor import IdDeDocente
from testes.fabricas import FabricaTesteModeloDocente, FabricaTesteIdDeDocente


class TestRotaDocente(APITestCase):
    @staticmethod
    def contruir_url(id_: UUID) -> str:
        return reverse('docente', kwargs={'id_': str(id_)})

    @staticmethod
    def construir_url_aleatoria() -> str:
        id_: IdDeDocente = FabricaTesteIdDeDocente.build()
        return TestRotaDocente.contruir_url(id_.valor)

    def test_get_QUANDO_id_existe_ENTAO_retorna_status_200(self) -> None:
        modelo_docente: ModeloDocente = FabricaTesteModeloDocente.create()
        url = self.contruir_url(id_=modelo_docente.id)

        response = self.client.get(path=url)

        self.assertEqual(response.status_code, 200)

    def test_get_QUANDO_id_existe_ENTAO_retorna_payload_esperado(self) -> None:
        modelo_docente: ModeloDocente = FabricaTesteModeloDocente.create()
        url = self.contruir_url(id_=modelo_docente.id)

        response = self.client.get(path=url)

        payload_resultante = json.loads(response.content)
        payload_esperado = {
            'id': modelo_docente.id,
            'nome': modelo_docente.nome
        }
        self.assertEqual(payload_resultante, payload_esperado)

    def test_get_QUANDO_id_nao_existe_ENTAO_retorna_status_404(self) -> None:
        url = self.construir_url_aleatoria()

        response = self.client.get(url)

        self.assertEqual(response.status_code, 404)
