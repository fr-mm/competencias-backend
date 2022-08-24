from dataclasses import dataclass

from dominio.otds.otd_base import OTDBase
from dominio.entidades import Docente


@dataclass
class OTDEntradaCasoDeUsoCriarDocente(OTDBase):
    nome: str

    def para_entidade(self) -> Docente:
        return Docente.construir(
            nome=self.nome
        )
