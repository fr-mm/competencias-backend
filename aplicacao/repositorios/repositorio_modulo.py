from typing import List

from aplicacao.models import ModeloModulo, ModeloDisciplinaEmModulo, ModeloDisciplina
from aplicacao.servicos import ServicoConverterModeloModulo
from dominio.entidades import Curso, Modulo
from dominio.erros import ErroModuloNaoEncontrado
from dominio.repositorios import RepositorioAbstratoModulo


class RepositorioModulo(RepositorioAbstratoModulo):
    def trazer_por_curso(self, curso: Curso) -> List[Modulo]:
        modelos: List[ModeloModulo] = [ModeloModulo.objects.get(pk=modulo_id.valor) for modulo_id in curso.modulos_ids]
        return [ServicoConverterModeloModulo.para_entidade(modelo) for modelo in modelos]

    def deletar(self, modulo: Modulo) -> None:
        try:
            modelo: ModeloModulo = ModeloModulo.objects.get(pk=modulo.id.valor)
            modelo.delete()
        except ModeloModulo.DoesNotExist:
            raise ErroModuloNaoEncontrado(id_=modulo.id.valor)

    def salvar(self, modulo: Modulo) -> None:
        modelo = ServicoConverterModeloModulo.de_entidade(modulo)
        disciplinas_em_modulo: List[ModeloDisciplinaEmModulo] = ModeloDisciplinaEmModulo.objects.filter(modulo_id=modulo.id.valor)
        self.__remover_disciplinas_apagadas(
            modulo=modulo,
            disciplinas_em_modulo=disciplinas_em_modulo
        )
        self.__adicionar_disciplinas_novas(
            modulo=modulo,
            modelo_modulo=modelo,
            disciplinas_em_modulo=disciplinas_em_modulo
        )
        modelo.save()

    @staticmethod
    def __remover_disciplinas_apagadas(modulo: Modulo, disciplinas_em_modulo: List[ModeloDisciplinaEmModulo]) -> None:
        [
            disciplina_em_modulo.delete() for disciplina_em_modulo in disciplinas_em_modulo if disciplina_em_modulo.disciplina.id not in [
                disciplina_id.valor for disciplina_id in modulo.disciplinas_ids
            ]
        ]

    @staticmethod
    def __adicionar_disciplinas_novas(
            modulo: Modulo,
            modelo_modulo: ModeloModulo,
            disciplinas_em_modulo: List[ModeloDisciplinaEmModulo]
    ) -> None:
        ids_das_disciplinas_no_modulo = [disciplina_em_modulo.disciplina.id for disciplina_em_modulo in disciplinas_em_modulo]
        for disciplina_id in modulo.disciplinas_ids:
            if disciplina_id.valor not in ids_das_disciplinas_no_modulo:
                modelo_disciplina = ModeloDisciplina.objects.get(pk=disciplina_id.valor)
                ModeloDisciplinaEmModulo(modulo=modelo_modulo, disciplina=modelo_disciplina).save()
