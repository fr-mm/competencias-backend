from random import randint
from uuid import uuid4

import factory

from dominio.otds import OTDCurso


class FabricaTesteOTDCurso(factory.Factory):
    class Meta:
        model = OTDCurso

    id = factory.Faker('uuid4', cast_to=None)
    nome = factory.Faker('name')
    modulos_ids = factory.List([factory.Faker('uuid4', cast_to=None) for _ in range(randint(1, 6))])
    ativo = factory.Faker('pybool')
