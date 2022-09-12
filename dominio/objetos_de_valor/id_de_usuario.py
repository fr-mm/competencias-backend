from dataclasses import dataclass, field
from uuid import uuid4, UUID


@dataclass(frozen=True)
class IdDeUsuario:
    valor: UUID = field(default_factory=uuid4)
