from uuid import UUID

from aplicacao.models import ModeloDocente, ModeloUnidadeSenai, ModeloTelefone
from dominio.entidades import Docente


class ServicoConverterModeloDocente:
    @staticmethod
    def de_entidade(entidade: Docente) -> ModeloDocente:
        unidade_senai = ModeloUnidadeSenai.objects.get(pk=entidade.unidade_senai_id.valor)
        return ModeloDocente(
            nome=entidade.nome.valor,
            id=entidade.id.valor,
            email=entidade.email.valor,
            tipo_de_contratacao=entidade.tipo_de_contratacao.valor.value,
            unidade_senai=unidade_senai,
            ativo=entidade.ativo
        )

    @staticmethod
    def para_entidade(modelo: ModeloDocente) -> Docente:
        id_ = UUID(str(modelo.id))
        telefones = ModeloTelefone.objects.filter(docente_id=id_)
        return Docente.construir(
            nome=str(modelo.nome),
            id_=id_,
            email=modelo.email,
            telefones=[telefone.numero for telefone in telefones],
            tipo_de_contratacao=str(modelo.tipo_de_contratacao),
            unidade_senai_id=modelo.unidade_senai.id,
            ativo=bool(modelo.ativo)
        )
