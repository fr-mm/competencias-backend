from typing import List

from aplicacao.models import ModeloDocente, ModeloTelefone
from aplicacao.servicos import ServicoConverterModeloDocente
from dominio.erros import ErroDocenteNaoEncontrado
from dominio.repositorios import RepositorioAbstratoDocente
from dominio.entidades import Docente
from dominio.objetos_de_valor import Id


class RepositorioDocente(RepositorioAbstratoDocente):
    def filtrar(self, **kwargs) -> [Docente]:
        modelos_docentes: List[ModeloDocente] = ModeloDocente.objects.filter(**kwargs)
        return [ServicoConverterModeloDocente.para_entidade(modelo) for modelo in modelos_docentes]

    def trazer_por_id(self, id_: Id) -> Docente:
        try:
            modelo: ModeloDocente = ModeloDocente.objects.get(pk=id_.valor)
            return ServicoConverterModeloDocente.para_entidade(modelo)
        except ModeloDocente.DoesNotExist:
            raise ErroDocenteNaoEncontrado(id_.valor)

    def salvar(self, docente: Docente) -> None:
        modelo_docente: ModeloDocente = ServicoConverterModeloDocente.de_entidade(docente)
        modelo_docente.save()
        modelos_telefones_existentes: List[ModeloTelefone] = ModeloTelefone.objects.filter(docente_id=docente.id.valor)
        self.__remover_telefones_apagados(
            docente=docente, modelos_telefones=modelos_telefones_existentes
        )
        self.__adicionar_telefones_novos(
            docente=docente,
            modelo_docente=modelo_docente,
            modelos_telefones=modelos_telefones_existentes
        )

    @staticmethod
    def __remover_telefones_apagados(docente: Docente, modelos_telefones: List[ModeloTelefone]) -> None:
        [
            modelo_telefone.delete() for modelo_telefone in modelos_telefones if modelo_telefone.numero not in [
                telefone.valor for telefone in docente.telefones
            ]
        ]

    @staticmethod
    def __adicionar_telefones_novos(
            docente: Docente,
            modelo_docente: ModeloDocente,
            modelos_telefones: List[ModeloTelefone]
    ) -> None:
        [
            ModeloTelefone(
                numero=telefone.valor,
                docente=modelo_docente
            ).save() for telefone in docente.telefones if telefone.valor not in [
                modelo_telefone.numero for modelo_telefone in modelos_telefones
            ]
        ]
