from abc import ABC, abstractmethod
from typing import List

from dominio.entidades import Competencia
from dominio.objetos_de_valor import Id


class RepositorioAbstratoCompetencia(ABC):
    @abstractmethod
    def salvar(self, *competencias) -> None:
        pass

    @abstractmethod
    def trazer_id_de_docente(self, id_docente: Id) -> List[Competencia]:
        pass

    @abstractmethod
    def deletar_todos_de_docente(self, id_docente: Id) -> None:
        pass
