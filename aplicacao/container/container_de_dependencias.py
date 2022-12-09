from dataclasses import dataclass

from aplicacao.repositorios import RepositorioDocente, RepositorioDisciplina, RepositorioCurso
from dominio.casos_de_uso import CasoDeUsoCriarDocente, CasoDeUsoFiltrarDocentes, CasoDeUsoTrazerDocente, \
    CasoDeUsoDesativarDocente, CasoDeUsoEditarDisciplina, CasoDeUsoEditarDocente, CasoDeUsoCriarDisciplina, \
    CasoDeUsoDesativarDisciplina, CasoDeUsoCriarCurso, CasoDeUsoEditarCurso, CasoDeUsoDesativarCurso


@dataclass(frozen=True, init=False)
class ContainerBase:
    pass


class Repositorios(ContainerBase):
    docentes = RepositorioDocente()
    disciplinas = RepositorioDisciplina()
    cursos = RepositorioCurso()


class CasosDeUsoDocente(ContainerBase):
    criar = CasoDeUsoCriarDocente(Repositorios.docentes)
    filtrar = CasoDeUsoFiltrarDocentes(Repositorios.docentes)
    trazer = CasoDeUsoTrazerDocente(Repositorios.docentes)
    editar = CasoDeUsoEditarDocente(Repositorios.docentes)
    desativar = CasoDeUsoDesativarDocente(Repositorios.docentes)


class CasosDeUsoDisciplina(ContainerBase):
    criar = CasoDeUsoCriarDisciplina(Repositorios.disciplinas)
    editar = CasoDeUsoEditarDisciplina(Repositorios.disciplinas)
    desativar = CasoDeUsoDesativarDisciplina(Repositorios.disciplinas)


class CasosDeUsoCurso(ContainerBase):
    criar = CasoDeUsoCriarCurso(Repositorios.cursos)
    editar = CasoDeUsoEditarCurso(Repositorios.cursos)
    desativar = CasoDeUsoDesativarCurso(Repositorios.cursos)


class CasosDeUso(ContainerBase):
    docente = CasosDeUsoDocente()
    disciplina = CasosDeUsoDisciplina()
    curso = CasosDeUsoCurso()


class ContainerDeDependencias(ContainerBase):
    repositorios = Repositorios()
    casos_de_uso = CasosDeUso()


container_de_dependencias = ContainerDeDependencias()
