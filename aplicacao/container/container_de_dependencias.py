from dataclasses import dataclass

from aplicacao.repositorios import RepositorioDocente, RepositorioDisciplina
from dominio.casos_de_uso import CasoDeUsoCriarDocente, CasoDeUsoFiltrarDocentes, CasoDeUsoTrazerDocente, \
    CasoDeUsoDesativarDocente, CasoDeUsoEditarDisciplina, CasoDeUsoEditarDocente, CasoDeUsoCriarDisciplina, \
    CasoDeUsoDesativarDisciplina


@dataclass(frozen=True, init=False)
class ContainerBase:
    pass


class Repositorios(ContainerBase):
    docentes = RepositorioDocente()
    disciplinas = RepositorioDisciplina()


class CasoDeUsoDocente(ContainerBase):
    criar = CasoDeUsoCriarDocente(Repositorios.docentes)
    filtrar = CasoDeUsoFiltrarDocentes(Repositorios.docentes)
    trazer = CasoDeUsoTrazerDocente(Repositorios.docentes)
    editar = CasoDeUsoEditarDocente(Repositorios.docentes)
    desativar = CasoDeUsoDesativarDocente(Repositorios.docentes)


class CasoDeUsoDisciplina(ContainerBase):
    criar = CasoDeUsoCriarDisciplina(Repositorios.disciplinas)
    editar = CasoDeUsoEditarDisciplina(Repositorios.disciplinas)
    desativar = CasoDeUsoDesativarDisciplina(Repositorios.disciplinas)


class CasosDeUso(ContainerBase):
    docente = CasoDeUsoDocente()
    disciplina = CasoDeUsoDisciplina()


class ContainerDeDependencias(ContainerBase):
    repositorios = Repositorios()
    casos_de_uso = CasosDeUso()


container_de_dependencias = ContainerDeDependencias()
