from django.core.management.base import BaseCommand

from pinax.invitations.models import InvitationStat


class Command(BaseCommand):
    help = "Adds invites to all users who don't have infinite invites."

    def add_arguments(self, parser):
        parser.add_argument(
            "num_invites",
            type=int,
            help="Number of invites to add"
        )

    def handle(self, *args, **options):
        InvitationStat.add_invites(options["num_invites"])
