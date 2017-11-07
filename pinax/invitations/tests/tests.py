from django.contrib.auth.models import User
from django.core.management import call_command
from django.test import TestCase

from account.models import SignupCode
from pinax.invitations.models import InvitationStat, JoinInvitation


class TestsJoinInvitation(TestCase):

    def setUp(self):
        self.to_user = User.objects.create(username="foo1")
        self.from_user = User.objects.create(username="foo2")
        self.signup_code = SignupCode.create(email="me@you.com")
        self.signup_code.save()
        self.status = JoinInvitation.STATUS_ACCEPTED
        self.invitation = JoinInvitation.objects.create(
            from_user=self.from_user,
            status=self.status,
            signup_code=self.signup_code,
        )

    def test_accept(self):
        self.invitation.accept(self.to_user)
        self.assertEqual(self.from_user.invitationstat.invites_accepted, 1)

    def test_process_independent_joins(self):
        JoinInvitation.process_independent_joins(self.to_user, "me@you.com")
        invite = JoinInvitation.objects.get(pk=self.invitation.pk)
        self.assertEqual(invite.status, JoinInvitation.STATUS_JOINED_INDEPENDENTLY)


class TestsManagement(TestCase):

    def test_topoff_invites(self):
        """
        Ensure correct number of invites after topoff.
        """
        user = User.objects.create(username="eldarion")
        call_command("topoff_invites", "10")
        call_command("topoff_invites", "10")
        istat = InvitationStat.objects.get(user=user)
        self.assertEqual(istat.invites_remaining(), 10)

    def test_add_invites(self):
        """
        Ensure correct number of invites after adding.
        """
        user = User.objects.create(username="eldarion")
        call_command("add_invites", "10")
        call_command("add_invites", "10")
        istat = InvitationStat.objects.get(user=user)
        self.assertEqual(istat.invites_remaining(), 20)
