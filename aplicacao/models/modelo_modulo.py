from django.db import models


class ModeloModulo(models.Model):
    id = models.UUIDField(primary_key=True, unique=True)
    numero = models.IntegerField()
