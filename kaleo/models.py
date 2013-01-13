from django.db import models
from django.conf import settings
from django.utils import timezone

from django.contrib.auth.models import User

from account.models import SignupCode

from kaleo.signals import invite_sent


DEFAULT_INVITE_EXPIRATION = getattr(settings, "KALEO_DEFAULT_EXPIRATION", 168)  # 168 Hours = 7 Days
DEFAULT_INVITE_ALLOCATION = getattr(settings, "KALEO_DEFAULT_INVITE_ALLOCATION", 0)


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
    
    from_user = models.ForeignKey(User, related_name="invites_sent")
    to_user = models.ForeignKey(User, null=True, related_name="invites_received")
    message = models.TextField(null=True)
    sent = models.DateTimeField(default=timezone.now)
    status = models.IntegerField(choices=INVITE_STATUS_CHOICES)
    signup_code = models.OneToOneField(SignupCode)
    
    def to_user_email(self):
        return self.signup_code.email
    
    @classmethod
    def invite(cls, from_user, to_email, message=None):
        if not from_user.invitationstat.can_send():
            raise NotEnoughInvitationsError()
        
        signup_code = SignupCode.create(
            email=to_email,
            inviter=from_user,
            expiry=DEFAULT_INVITE_EXPIRATION,
            check_exists=False  # before we are called caller must check for existence
        )
        signup_code.save()
        join = cls.objects.create(
            from_user=from_user,
            message=message,
            status=JoinInvitation.STATUS_SENT,
            signup_code=signup_code
        )
        signup_code.send()
        stat = from_user.invitationstat
        stat.invites_sent += 1
        stat.save()
        invite_sent.send(sender=cls, invitation=join)
        return join


class InvitationStat(models.Model):
    
    user = models.OneToOneField(User)
    invites_sent = models.IntegerField(default=0)
    invites_allocated = models.IntegerField(default=DEFAULT_INVITE_ALLOCATION)
    invites_accepted = models.IntegerField(default=0)
    
    def invites_remaining(self):
        if self.invites_allocated == -1:
            return -1
        return self.invites_allocated - self.invites_sent
    
    def can_send(self):
        if self.invites_allocated == -1:
            return True
        return self.invites_allocated > self.invites_sent
    can_send.boolean = True
