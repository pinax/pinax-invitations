import sys

from django.core.management.base import BaseCommand

from pinax.invitations.models import InvitationStat


class Command(BaseCommand):
    help = "Adds invites to all users with 0 invites remaining."

    def handle(self, *args, **kwargs):
        if len(args) == 0:
            sys.exit("You must supply the number of invites as an argument.")

        try:
            num_of_invites = int(args[0])
        except ValueError:
            sys.exit("The argument for number of invites must be an integer.")

        InvitationStat.add_invites(num_of_invites)
