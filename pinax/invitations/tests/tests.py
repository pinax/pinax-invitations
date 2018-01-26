from django.contrib.auth.models import User
from django.core.management import call_command

from account.models import SignupCode
from pinax.invitations.forms import InviteForm
from pinax.invitations.models import InvitationStat, JoinInvitation
from test_plus.test import TestCase


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


class FormTests(TestCase):

    def test_already_invited(self):
        """Ensure form is not valid if invite has already been sent"""
        from_user = User.objects.create(username="eldarion")
        to_user = User.objects.create(username="invitee", email="invitee@example.com")
        InvitationStat.add_invites(2)
        istat = from_user.invitationstat
        istat.refresh_from_db()

        # Create an existing invitation
        JoinInvitation.invite(from_user, to_user.email, send=False)

        # Attempt to invite same user again
        form_data = {
            "email_address": to_user.email
        }
        form = InviteForm(user=from_user, data=form_data)
        self.assertFalse(form.is_valid())


class ViewTests(TestCase):

    def test_invite_view(self):
        """verify no errors when posting good form data"""
        user = self.make_user("amy")
        InvitationStat.add_invites(2)
        post_data = {
            "email_address": "amy@example.com"
        }
        with self.login(user):
            self.post("pinax_invitations:invite", data=post_data)
            self.response_200()

    def test_invite_view_bad_data(self):
        """verify no errors when posting bad data"""
        user = self.make_user("sandee")
        post_data = {
        }
        with self.login(user):
            self.post("pinax_invitations:invite", data=post_data)
            self.response_200()
