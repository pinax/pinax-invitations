from django.test import TestCase

from django.contrib.auth.models import User

from account.models import SignupCode

from pinax.invitations.models import JoinInvitation


class TestsJoinInvitation(TestCase):

    def setUp(self):
        self.to_user = User.objects.create(username='foo1')
        self.from_user = User.objects.create(username='foo2')
        self.signup_code = SignupCode.create(email="me@you.com")
        self.signup_code.save()
        self.status = JoinInvitation.STATUS_ACCEPTED
        self.invitation = JoinInvitation.objects.create(
            from_user=self.from_user,
            status=self.status,
            signup_code=self.signup_code,
        )

    def test_to_user_email(self):
        self.assertEqual(self.signup_code.email, "me@you.com")

    def test_accept(self):
        self.invitation.accept(self.to_user)
        self.assertEqual(self.from_user.invitationstat.invites_accepted, 1)

    def test_process_independent_joins(self):
        JoinInvitation.process_independent_joins(self.to_user, "me@you.com")
        invite = JoinInvitation.objects.get(pk=self.invitation.pk)
        self.assertEqual(invite.status, JoinInvitation.STATUS_JOINED_INDEPENDENTLY)
