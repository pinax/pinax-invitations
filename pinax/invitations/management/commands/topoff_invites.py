from django.core.management.base import BaseCommand

from pinax.invitations.models import InvitationStat


class Command(BaseCommand):
    help = "Ensure all users have a minimum number of invites."

    def add_arguments(self, parser):
        parser.add_argument(
            "num_invites",
            type=int,
            help="Minimum number of invites"
        )

    def handle(self, *args, **options):
        InvitationStat.topoff(options["num_invites"])
