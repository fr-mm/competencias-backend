from dataclasses import dataclass

from aplicacao.repositorios import RepositorioDocente
from dominio.casos_de_uso import CasoDeUsoCriarDocente, CasoDeUsoFiltrarDocentes, CasoDeUsoTrazerDocente


@dataclass(frozen=True, init=False)
class ContainerBase:
    pass


class Repositorios(ContainerBase):
    docentes = RepositorioDocente()


class CasosDeUso(ContainerBase):
    criar_docente = CasoDeUsoCriarDocente(Repositorios.docentes)
    filtrar_docentes = CasoDeUsoFiltrarDocentes(Repositorios.docentes)
    trazer_docente = CasoDeUsoTrazerDocente(Repositorios.docentes)


class ContainerDeDependencias(ContainerBase):
    repositorios = Repositorios()
    casos_de_uso = CasosDeUso()


container_de_dependencias = ContainerDeDependencias()
