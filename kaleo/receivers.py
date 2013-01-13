from django.db.models.signals import post_save
from django.dispatch import receiver

from django.contrib.auth.models import User

from account.models import SignupCodeResult, EmailConfirmation
from account.signals import signup_code_used, email_confirmed

from kaleo.models import JoinInvitation, InvitationStat
from kaleo.signals import invite_accepted


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
