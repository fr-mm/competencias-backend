from dataclasses import dataclass

from aplicacao.repositorios import RepositorioDocente
from dominio.casos_de_uso import CasoDeUsoCriarDocente, CasoDeUsoTrazerDocentes, CasoDeUsoTrazerDocente


@dataclass(frozen=True, init=False)
class ContainerBase:
    pass


class Repositorios(ContainerBase):
    docentes = RepositorioDocente()


class CasosDeUso(ContainerBase):
    criar_docente = CasoDeUsoCriarDocente(Repositorios.docentes)
    trazer_docentes = CasoDeUsoTrazerDocentes(Repositorios.docentes)
    trazer_docente = CasoDeUsoTrazerDocente(Repositorios.docentes)


class ContainerDeDependencias(ContainerBase):
    repositorios = Repositorios()
    casos_de_uso = CasosDeUso()


container_de_dependencias = ContainerDeDependencias()
