from typing import List

from aplicacao.models import ModeloCurso, ModeloModuloEmCurso, ModeloModulo, ModeloDisciplinaEmModulo, ModeloDisciplina
from aplicacao.servicos import ServicoConverterModeloCurso, ServicoConverterModeloModulo
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
        self.__editar_modulos(curso, modelo_curso)

    def __editar_modulos(self, curso: Curso, modelo_curso: ModeloCurso) -> None:
        self.__adicionar_modulos_novos(
            curso=curso,
            modelo_curso=modelo_curso
        )


    @staticmethod
    def __adicionar_modulos_novos(
            curso: Curso,
            modelo_curso: ModeloCurso,
    ) -> None:
        [ModeloModulo.objects.get(pk=modulo_em_curso.modulo.id).delete() for modulo_em_curso in ModeloModuloEmCurso.objects.filter(curso=modelo_curso)]
        for modulo in curso.modulos:
            modelo_modulo = ServicoConverterModeloModulo.de_entidade(modulo)
            modelo_modulo.save()
            modulo_em_curso = ModeloModuloEmCurso(curso=modelo_curso, modulo=modelo_modulo)
            modulo_em_curso.save()
            for disciplina_id in modulo.disciplinas_ids:
                modelo_disciplina = ModeloDisciplina.objects.get(pk=disciplina_id.valor)
                ModeloDisciplinaEmModulo(modulo=modelo_modulo, disciplina=modelo_disciplina).save()
