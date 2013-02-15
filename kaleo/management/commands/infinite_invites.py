import sys

from django.core.management.base import BaseCommand

from kaleo.models import InvitationStat
from .compat import get_user_model


class Command(BaseCommand):
    help = "Sets invites_allocated to -1 to represent infinite invites."
    
    def handle(self, *args, **kwargs):
        for user in get_user_model().objects.all():
            stat, _ = InvitationStat.objects.get_or_create(user=user)
            stat.invites_allocated = -1
            stat.save()
