from __future__ import annotations

from uuid import UUID

from aplicacao.models import UsuarioBase
from dominio.entidades import Usuario


class ModeloUsuario(UsuarioBase):
    @classmethod
    def de_entidade(cls, entidade: Usuario) -> ModeloUsuario:
        return cls(
            id=entidade.id.valor,
            nome=entidade.nome.valor,
            email=entidade.email.valor,
            is_active=entidade.ativo
        )

    def para_entidade(self) -> Usuario:
        return Usuario.construir(
            id_=UUID(str(self.id)),
            nome=str(self.nome),
            email=str(self.email),
            ativo=bool(self.is_active)
        )

    @property
    def ativo(self) -> bool:
        return self.is_active

    @ativo.setter
    def ativo(self, ativo: bool) -> None:
        self.is_active = ativo
