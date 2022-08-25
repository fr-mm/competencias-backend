from __future__ import annotations

from dataclasses import dataclass

from dominio.entidades import Docente
from dominio.otds.otd_docente import OTDDocente


@dataclass
class OTDTrazerDocentesSaida:
    docentes: [OTDDocente]

    @classmethod
    def de_entidades(cls, docentes: [Docente]) -> OTDTrazerDocentesSaida:
        return cls([OTDDocente.de_entidade(docente) for docente in docentes])
