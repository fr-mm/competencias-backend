from dataclasses import dataclass, field

from dominio.objetos_de_valor import NomeDeDocente, IdDeDocente


@dataclass(frozen=True)
class Docente:
    nome: NomeDeDocente
    id: IdDeDocente = field(default_factory=IdDeDocente)
