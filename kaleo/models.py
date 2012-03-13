from django.db import models
from django.db.models.signals import post_save
from django.conf import settings
from django.dispatch import receiver
from django.utils import timezone

from django.contrib.auth.models import User

from account.models import SignupCode, SignupCodeResult, EmailConfirmation
from account.signals import signup_code_used, email_confirmed
from kaleo.signals import invite_sent, invite_accepted


DEFAULT_INVITE_EXPIRATION = getattr(settings, "KALEO_DEFAULT_EXPIRATION", 168) # 168 Hours = 7 Days
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
            check_exists=False # before we are called caller must check for existence
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


@receiver(signup_code_used, sender=SignupCodeResult)
def handle_signup_code_used(sender, **kwargs):
    result = kwargs.get("signup_code_result")
    try:
        invite = result.signup_code.joininvitation
        invite.to_user = result.user
        invite.status = JoinInvitation.STATUS_ACCEPTED
        invite.save()
        stat = invite.from_user.invitationstat
        stat.invites_accepted += 1
        stat.save()
        invite_accepted.send(sender=JoinInvitation, invitation=invite)
    except JoinInvitation.DoesNotExist:
        pass


@receiver(email_confirmed, sender=EmailConfirmation)
def handle_email_confirmed(sender, **kwargs):
    email_address = kwargs.get("email_address")
    invites = JoinInvitation.objects.filter(
        to_user__isnull=True,
        signup_code__email=email_address.email
    )
    for invite in invites:
        invite.to_user = email_address.user
        invite.status = JoinInvitation.STATUS_JOINED_INDEPENDENTLY
        invite.save()


@receiver(post_save, sender=User)
def create_stat(sender, instance=None, **kwargs):
    if instance is None:
        return
    InvitationStat.objects.get_or_create(user=instance)
