import sys

from django.core.management.base import BaseCommand

from django.contrib.auth.models import User

from kaleo.models import InvitationStat


class Command(BaseCommand):
    help = "Sets invites_allocated to -1 to represent infinite invites."
    
    def handle(self, *args, **kwargs):
        for user in User.objects.all():
            stat, _ = InvitationStat.objects.get_or_create(user=user)
            stat.invites_allocated = -1
            stat.save()
