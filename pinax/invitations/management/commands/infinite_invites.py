from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

from pinax.invitations.models import InvitationStat


class Command(BaseCommand):
    help = "Sets all users to have infinite invites."

    def handle(self, *args, **options):
        for user in get_user_model().objects.all():
            stat, _ = InvitationStat.objects.get_or_create(user=user)
            stat.invites_allocated = -1
            stat.save()
