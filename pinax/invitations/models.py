from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

from account.models import SignupCode

from .conf import settings
from .signals import invite_sent, joined_independently, invite_accepted


class NotEnoughInvitationsError(Exception):
    pass


class JoinInvitation(models.Model):

    STATUS_SENT = 1
    STATUS_ACCEPTED = 2
    STATUS_JOINED_INDEPENDENTLY = 3

    INVITE_STATUS_CHOICES = [
        (STATUS_SENT, "Sent"),
        (STATUS_ACCEPTED, "Accepted"),
        (STATUS_JOINED_INDEPENDENTLY, "Joined Independently")
    ]

    from_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="invites_sent")
    to_user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, related_name="invites_received")
    message = models.TextField(null=True)
    sent = models.DateTimeField(default=timezone.now)
    status = models.IntegerField(choices=INVITE_STATUS_CHOICES)
    signup_code = models.OneToOneField(SignupCode)

    def to_user_email(self):
        return self.signup_code.email

    def accept(self, user):
        self.to_user = user
        self.status = JoinInvitation.STATUS_ACCEPTED
        self.save()
        self.from_user.invitationstat.increment_accepted()
        invite_accepted.send(sender=JoinInvitation, invitation=self)

    @classmethod
    def process_independent_joins(cls, user, email):
        invites = cls.objects.filter(
            to_user__isnull=True,
            signup_code__email=email
        )
        for invite in invites:
            invite.to_user = user
            invite.status = cls.STATUS_JOINED_INDEPENDENTLY
            invite.save()
            joined_independently.send(sender=cls, invitation=invite)

    @classmethod
    def invite(cls, from_user, to_email, message=None, send=True):
        if not from_user.invitationstat.can_send():
            raise NotEnoughInvitationsError()

        signup_code = SignupCode.create(
            email=to_email,
            inviter=from_user,
            expiry=settings.PINAX_INVITATIONS_DEFAULT_EXPIRATION,
            check_exists=False  # before we are called caller must check for existence
        )
        signup_code.save()
        join = cls.objects.create(
            from_user=from_user,
            message=message,
            status=JoinInvitation.STATUS_SENT,
            signup_code=signup_code
        )

        def send_invite(*args, **kwargs):
            signup_code.send(*args, **kwargs)
            InvitationStat.objects.filter(user=from_user).update(
                invites_sent=models.F("invites_sent") + 1
            )
            invite_sent.send(sender=cls, invitation=join)
        if send:
            send_invite()
        else:
            join.send_invite = send_invite
        return join


class InvitationStat(models.Model):

    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    invites_sent = models.IntegerField(default=0)
    invites_allocated = models.IntegerField(default=settings.PINAX_INVITATIONS_DEFAULT_INVITE_ALLOCATION)
    invites_accepted = models.IntegerField(default=0)

    def increment_accepted(self):
        self.invites_accepted += 1
        self.save()

    @classmethod
    def add_invites_to_user(cls, user, amount):
        stat, _ = InvitationStat.objects.get_or_create(user=user)
        if stat.invites_allocated != -1:
            stat.invites_allocated += amount
            stat.save()

    @classmethod
    def add_invites(cls, amount):
        for user in get_user_model().objects.all():
            cls.add_invites_to_user(user, amount)

    @classmethod
    def topoff_user(cls, user, amount):
        "Makes sure user has a certain number of invites"
        stat, _ = cls.objects.get_or_create(user=user)
        remaining = stat.invites_remaining()
        if remaining != -1 and remaining < amount:
            stat.invites_allocated += (amount - remaining)
            stat.save()

    @classmethod
    def topoff(cls, amount):
        "Makes sure all users have a certain number of invites"
        for user in get_user_model().objects.all():
            cls.topoff_user(user, amount)

    def invites_remaining(self):
        if self.invites_allocated == -1:
            return -1
        return self.invites_allocated - self.invites_sent

    def can_send(self):
        if self.invites_allocated == -1:
            return True
        return self.invites_allocated > self.invites_sent
    can_send.boolean = True
