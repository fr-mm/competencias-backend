from dataclasses import dataclass
from typing import List
from uuid import UUID

from dominio.otds.otd_competencia import OTDCompetencia


@dataclass
class OTDCasoDeUsoEditarCompetencias:
    docente_id: UUID
    competencias: List[OTDCompetencia]
