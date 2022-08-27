from abc import ABC, abstractmethod

from dominio.entidades import Docente
from dominio.objetos_de_valor import IdDeDocente


class RepositorioAbstratoDocente(ABC):
    @abstractmethod
    def trazer(self) -> [Docente]:
        pass

    @abstractmethod
    def trazer_por_id(self, id_: IdDeDocente) -> Docente:
        pass

    @abstractmethod
    def salvar(self, docente: Docente) -> None:
        pass

    @abstractmethod
    def deletar_por_id(self, id_: IdDeDocente) -> None:
        pass

    @abstractmethod
    def id_existe(self, id_: IdDeDocente) -> bool:
        pass
