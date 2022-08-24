from dataclasses import dataclass

from dominio.entidades import Docente


@dataclass
class OTDCriarDocenteEntrada:
    nome: str

    def para_entidade(self) -> Docente:
        return Docente.construir(
            nome=self.nome
        )
