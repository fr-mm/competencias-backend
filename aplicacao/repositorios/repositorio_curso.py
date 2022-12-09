from typing import List

from aplicacao.models import ModeloCurso, ModeloModuloEmCurso, ModeloModulo
from aplicacao.servicos import ServicoConverterModeloCurso
from dominio.entidades import Curso
from dominio.erros import ErroCursoNaoEncontrado
from dominio.objetos_de_valor import Id
from dominio.repositorios import RepositorioAbstratoCurso


class RepositorioCurso(RepositorioAbstratoCurso):
    def filtrar(self, **kwargs) -> [Curso]:
        modelos_cursos: List[ModeloCurso] = ModeloCurso.objects.filter(**kwargs)
        return [ServicoConverterModeloCurso.para_entidade(modelo) for modelo in modelos_cursos]

    def trazer_por_id(self, id_: Id) -> Curso:
        try:
            modelo: ModeloCurso = ModeloCurso.objects.get(pk=id_.valor)
            return ServicoConverterModeloCurso.para_entidade(modelo)
        except ModeloCurso.DoesNotExist:
            raise ErroCursoNaoEncontrado(id_.valor)

    def salvar(self, curso: Curso) -> None:
        modelo_curso = ServicoConverterModeloCurso.de_entidade(curso)
        modelo_curso.save()
        modulos_em_curso: List[ModeloModuloEmCurso] = ModeloModuloEmCurso.objects.filter(curso=modelo_curso)
        self.__remover_modulos_apagados(
            curso=curso,
            modulos_em_curso=modulos_em_curso
        )
        self.__adicionar_modulos_novos(
            curso=curso,
            modelo_curso=modelo_curso,
            modulos_em_curso=modulos_em_curso
        )

    @staticmethod
    def __remover_modulos_apagados(curso: Curso, modulos_em_curso: List[ModeloModuloEmCurso]) -> None:
        [
            modulo_em_curso.delete() for modulo_em_curso in modulos_em_curso if modulo_em_curso.modulo.id not in [
                id_.valor for id_ in curso.modulos_ids
            ]
        ]

    @staticmethod
    def __adicionar_modulos_novos(
            curso: Curso,
            modelo_curso: ModeloCurso,
            modulos_em_curso: List[ModeloModuloEmCurso]
    ) -> None:
        ids_dos_modulos_no_curso = [modulo_no_curso.modulo.id for modulo_no_curso in modulos_em_curso]
        for modulo_id in curso.modulos_ids:
            if modulo_id.valor not in ids_dos_modulos_no_curso:
                modelo_modulo = ModeloModulo.objects.get(pk=modulo_id.valor)
                modulo_em_curso = ModeloModuloEmCurso(curso=modelo_curso, modulo=modelo_modulo)
                modulo_em_curso.save()
