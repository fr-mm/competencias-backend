import json
from typing import Dict
from uuid import UUID

from django.urls import reverse
from rest_framework.test import APITestCase

from aplicacao.models import ModeloCurso, ModeloModulo, ModeloModuloEmCurso
from dominio.objetos_de_valor import Id
from dominio.otds import OTDCurso
from testes.fabricas import FabricaTesteId, FabricaTesteModeloCurso, FabricaTesteOTDCurso, FabricaTesteModeloModulo, \
    FabricaTesteModeloModuloEmCurso


class TestRotaCurso(APITestCase):
    @staticmethod
    def contruir_url(id_: UUID) -> str:
        return reverse('curso', kwargs={'id_': str(id_)})

    @staticmethod
    def construir_url_aleatoria() -> str:
        id_: Id = FabricaTesteId.build()
        return TestRotaCurso.contruir_url(id_.valor)

    @staticmethod
    def otd_para_request_data(otd: OTDCurso) -> Dict[str, any]:
        return {
            'id': str(otd.id),
            'nome': otd.nome,
            'modulos_ids': [str(id_) for id_ in otd.modulos_ids],
            'ativo': otd.ativo
        }

    def test_post_QUANDO_id_existe_ENTAO_retorna_status_200(self) -> None:
        otd_entrada: OTDCurso = FabricaTesteOTDCurso.build(ativo=True, modulos_ids=[])
        modelo: ModeloCurso = FabricaTesteModeloCurso.create(
            id=otd_entrada.id,
            ativo=otd_entrada.ativo
        )
        data = self.otd_para_request_data(otd_entrada)
        url = self.contruir_url(id_=modelo.id)

        response = self.client.post(
            path=url,
            data=json.dumps(data),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, 200)

    def test_post_QUANDO_nome_diferente_ENTAO_altera_no_banco_de_dados(self) -> None:
        nome_novo = 'Nome novo'
        modelo_antes: ModeloCurso = FabricaTesteModeloCurso.create(
            ativo=True
        )
        otd_entrada: OTDCurso = FabricaTesteOTDCurso.build(
            id=modelo_antes.id,
            nome=nome_novo,
            ativo=True,
            modulos_ids=[]
        )
        data = self.otd_para_request_data(otd_entrada)
        url = self.contruir_url(id_=modelo_antes.id)

        self.client.post(
            path=url,
            data=json.dumps(data),
            content_type='application/json'
        )

        modelo_depois: ModeloCurso = ModeloCurso.objects.get(pk=modelo_antes.id)
        self.assertEqual(modelo_depois.nome, nome_novo)

    def test_post_QUANDO_modulos_diferente_ENTAO_altera_no_banco_de_dados(self) -> None:
        modulo_existente: ModeloModulo = FabricaTesteModeloModulo.create()
        modulo_a_ser_deletado: ModeloModulo = FabricaTesteModeloModulo.create()
        modulo_novo: ModeloModulo = FabricaTesteModeloModulo.create()
        curso: ModeloCurso = FabricaTesteModeloCurso.create(
            ativo=True
        )
        modulo_em_curso_existente = FabricaTesteModeloModuloEmCurso.create(
            curso=curso,
            modulo=modulo_existente
        )
        modulo_em_curso_a_ser_deletado = FabricaTesteModeloModuloEmCurso.create(
            curso=curso,
            modulo=modulo_a_ser_deletado
        )
        otd_entrada: OTDCurso = FabricaTesteOTDCurso.build(
            id=curso.id,
            nome=curso.nome,
            modulos_ids=[modulo_existente.id, modulo_novo.id],
            ativo=True,
        )
        data = self.otd_para_request_data(otd_entrada)
        url = self.contruir_url(id_=curso.id)

        self.client.post(
            path=url,
            data=json.dumps(data),
            content_type='application/json'
        )

        print('exi', modulo_existente.id)
        print('del', modulo_a_ser_deletado.id)
        print('nov', modulo_novo.id)
        resultado = [modelo.modulo.id for modelo in ModeloModuloEmCurso.objects.all()]
        esperado = [modulo.id for modulo in [modulo_existente, modulo_novo]]
        self.assertEqual(resultado, esperado)
