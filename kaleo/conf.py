from __future__ import unicode_literals

from django.conf import settings  # noqa

from appconf import AppConf


class KaleoAppConf(AppConf):

    DEFAULT_EXPIRATION = 168
    DEFAULT_INVITE_ALLOCATION = 0
