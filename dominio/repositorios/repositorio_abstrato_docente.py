from abc import ABC, abstractmethod

from dominio.entidades import Docente
from dominio.objetos_de_valor import IdDeDocente


class RepositorioAbstratoDocente(ABC):
    @abstractmethod
    def filtrar(self, **kwargs) -> [Docente]:
        pass

    @abstractmethod
    def trazer_por_id(self, id_: IdDeDocente) -> Docente:
        """Lança ErroDocenteNaoEncontrado"""
        pass

    @abstractmethod
    def salvar(self, docente: Docente) -> None:
        pass
