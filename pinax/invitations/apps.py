import importlib

from django.apps import AppConfig as BaseAppConfig
from django.utils.translation import ugettext_lazy as _


class AppConfig(BaseAppConfig):

    label = "pinax_invitations"
    name = "pinax.invitations"
    verbose_name = _("Pinax Invitations")

    def ready(self):
        importlib.import_module("pinax.invitations.receivers")
