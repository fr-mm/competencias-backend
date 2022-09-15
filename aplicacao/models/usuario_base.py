from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy

from aplicacao.managers import UsuarioManager


class UsuarioBase(AbstractUser):
    username = None
    nome = models.CharField(max_length=150)
    email = models.EmailField(gettext_lazy('email_address'), unique=True)

    objects = UsuarioManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
