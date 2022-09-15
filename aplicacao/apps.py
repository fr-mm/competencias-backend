from django.apps import AppConfig
from django.db.models.signals import pre_save
from django.dispatch import receiver


class AplicacaoConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "aplicacao"
    label = 'aplicacao'

    def ready(self):
        UsuarioBase = self.get_model('UsuarioBase')
        pre_save.connect(receiver, sender='aplicacao.UsuarioBase')
        ModeloUsuario = self.get_model('ModeloUsuario')
        pre_save.connect(receiver, sender='aplicacao.ModeloUsuario')
