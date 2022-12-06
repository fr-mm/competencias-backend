from random import randint
from uuid import uuid4

import factory

from dominio.otds import OTDCurso


class FabricaTesteOTDCurso(factory.Factory):
    class Meta:
        model = OTDCurso

    id = factory.Faker('uuid4')
    nome = factory.Faker('name')
    modulos_ids = factory.List([uuid4() for _ in range(randint(1, 6))])
    ativo = factory.Faker('pybool')
