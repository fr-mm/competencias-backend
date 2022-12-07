from abc import ABC, abstractmethod
from typing import List

from dominio.entidades import Modulo, Curso


class RepositorioAbstratoModulo(ABC):
    @abstractmethod
    def salvar(self, modulo: Modulo) -> None:
        pass

    @abstractmethod
    def trazer_por_curso(self, curso: Curso) -> List[Modulo]:
        pass

    @abstractmethod
    def deletar(self, modulo: Modulo) -> None:
        pass
