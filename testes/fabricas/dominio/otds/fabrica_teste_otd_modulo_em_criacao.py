from random import randint
from uuid import uuid4

import factory

from dominio.otds import OTDModuloEmCriacao


class FabricaTesteOTDModuloEmCriacao(factory.Factory):
    class Meta:
        model = OTDModuloEmCriacao

    numero = factory.Faker('pyint', min_value=1, max_value=10)
    disciplinas_ids = factory.List([uuid4() for _ in range(randint(1, 6))])
