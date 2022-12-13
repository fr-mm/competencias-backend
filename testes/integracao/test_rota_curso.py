import json
from typing import Dict
from uuid import UUID

from django.urls import reverse
from rest_framework.test import APITestCase

from aplicacao.models import ModeloCurso, ModeloModulo, ModeloModuloEmCurso, ModeloDisciplina, ModeloDisciplinaEmModulo
from dominio.objetos_de_valor import Id
from dominio.otds import OTDCursoEntrada, OTDModuloEmCriacao
from testes.fabricas import FabricaTesteId, FabricaTesteModeloCurso, FabricaTesteOTDCursoEntrada, \
    FabricaTesteModeloModulo, \
    FabricaTesteModeloModuloEmCurso, FabricaTesteModeloDisciplina, FabricaTesteModeloDisciplinaEmModulo


class TestRotaCurso(APITestCase):
    @staticmethod
    def contruir_url(id_: UUID) -> str:
        return reverse('curso', kwargs={'id_': str(id_)})

    @staticmethod
    def construir_url_aleatoria() -> str:
        id_: Id = FabricaTesteId.build()
        return TestRotaCurso.contruir_url(id_.valor)

    @staticmethod
    def otd_para_request_data(otd: OTDCursoEntrada) -> Dict[str, any]:
        modulos = []
        for otd_modulo in otd.modulos:
            modulo = otd_modulo.__dict__
            modulo['disciplinas_ids'] = [str(id_) for id_ in modulo['disciplinas_ids']]
            modulos.append(modulo)

        return {
            'id': str(otd.id),
            'nome': otd.nome,
            'modulos': modulos,
            'ativo': otd.ativo
        }

    def test_post_QUANDO_id_existe_ENTAO_retorna_status_200(self) -> None:
        otd_entrada: OTDCursoEntrada = FabricaTesteOTDCursoEntrada.build(ativo=True, modulos=[])
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
        otd_entrada: OTDCursoEntrada = FabricaTesteOTDCursoEntrada.build(
            id=modelo_antes.id,
            nome=nome_novo,
            ativo=True,
            modulos=[]
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
        modulo_existente: ModeloModulo = FabricaTesteModeloModulo.create(numero=1)
        modulo_a_ser_deletado: ModeloModulo = FabricaTesteModeloModulo.create(numero=2)
        disciplinas: [ModeloDisciplina] = [FabricaTesteModeloDisciplina.create() for _ in range(3)]
        modelo_curso: ModeloCurso = FabricaTesteModeloCurso.create(
            ativo=True
        )
        FabricaTesteModeloModuloEmCurso.create(
            curso=modelo_curso,
            modulo=modulo_existente
        )
        FabricaTesteModeloModuloEmCurso.create(
            curso=modelo_curso,
            modulo=modulo_a_ser_deletado
        )
        FabricaTesteModeloDisciplinaEmModulo.create(
            modulo=modulo_existente,
            disciplina=disciplinas[0]
        )
        nome_novo = 'Nome novo'
        otd_entrada = OTDCursoEntrada(
            id=modelo_curso.id,
            nome=nome_novo,
            modulos=[
                OTDModuloEmCriacao(
                    numero=modulo_existente.numero,
                    disciplinas_ids=[disciplinas[1].id, disciplinas[2].id]
                ),
                OTDModuloEmCriacao(
                    numero=3,
                    disciplinas_ids=[]
                )
            ],
            ativo=modelo_curso.ativo
        )
        request_data = self.otd_para_request_data(otd_entrada)
        url = self.contruir_url(id_=modelo_curso.id)

        self.client.post(
            path=url,
            data=json.dumps(request_data),
            content_type='application/json'
        )

        curso_depois: ModeloCurso = ModeloCurso.objects.get(pk=modelo_curso.id)
        modulos_em_curso = [modulo_em_curso.modulo.id for modulo_em_curso in ModeloModuloEmCurso.objects.filter(curso=curso_depois)]
        modulos = [ModeloModulo.objects.get(pk=id_) for id_ in modulos_em_curso]
        modulo_1 = [modulo for modulo in modulos if modulo.numero == 1][0]
        resultado = {
            'nome': curso_depois.nome,
            'modulos': len(ModeloModuloEmCurso.objects.filter(curso=curso_depois)),
            'disciplinas_em_modulo_1': [
                disciplina_em_modulo.disciplina.id for disciplina_em_modulo in ModeloDisciplinaEmModulo.objects.filter(modulo=modulo_1)
            ]
        }
        esperado = {
            'nome': nome_novo,
            'modulos': 2,
            'disciplinas_em_modulo_1': [disciplinas[1].id, disciplinas[2].id]
        }
        self.assertEqual(resultado, esperado)
