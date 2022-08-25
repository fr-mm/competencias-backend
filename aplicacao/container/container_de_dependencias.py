from dataclasses import dataclass

from aplicacao.repositorios import RepositorioDocente
from dominio.casos_de_uso import CasoDeUsoCriarDocente


@dataclass(frozen=True, init=False)
class ContainerBase:
    pass


class Repositorios(ContainerBase):
    docentes = RepositorioDocente()


class CasosDeUso(ContainerBase):
    criar_docente = CasoDeUsoCriarDocente(Repositorios.docentes)
    trazer_docentes = CasoDeUsoCriarDocente(Repositorios.docentes)


class ContainerDeDependencias(ContainerBase):
    repositorios = Repositorios()
    casos_de_uso = CasosDeUso()


container_de_dependencias = ContainerDeDependencias()
