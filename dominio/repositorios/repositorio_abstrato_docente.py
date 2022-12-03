from abc import ABC, abstractmethod

from dominio.entidades import Docente
from dominio.objetos_de_valor import Id


class RepositorioAbstratoDocente(ABC):
    @abstractmethod
    def filtrar(self, **kwargs) -> [Docente]:
        pass

    @abstractmethod
    def trazer_por_id(self, id_: Id) -> Docente:
        """Lança ErroDocenteNaoEncontrado"""
        pass

    @abstractmethod
    def salvar(self, docente: Docente) -> None:
        pass
