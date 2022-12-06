from abc import ABC, abstractmethod

from dominio.entidades import Disciplina
from dominio.objetos_de_valor import Id


class RepositorioAbstratoDisciplina(ABC):
    @abstractmethod
    def filtrar(self, **kwargs) -> [Disciplina]:
        pass

    @abstractmethod
    def salvar(self, disciplina: Disciplina) -> None:
        pass

    @abstractmethod
    def trazer_por_id(self, id_: Id) -> Disciplina:
        pass

