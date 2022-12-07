from dataclasses import dataclass
from typing import List
from uuid import UUID


@dataclass(frozen=True)
class OTDIds:
    ids: List[UUID]
