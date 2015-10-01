from django import template

from pinax.invitations.forms import InviteForm
from pinax.invitations.models import InvitationStat


register = template.Library()


@register.inclusion_tag("pinax/invitations/_invites_remaining.html")
def invites_remaining(user):
    try:
        remaining = user.invitationstat.invites_remaining()
    except InvitationStat.DoesNotExist:
        remaining = 0
    return {"invites_remaining": remaining}


@register.inclusion_tag("pinax/invitations/_invite_form.html")
def invite_form(user):
    return {"form": InviteForm(user=user), "user": user}


@register.inclusion_tag("pinax/invitations/_invited.html")
def invites_sent(user):
    return {"invited_list": user.invites_sent.all()}


@register.filter
def status_class(invite):
    if invite.status == invite.STATUS_SENT:
        return "sent"
    elif invite.status == invite.STATUS_ACCEPTED:
        return "accepted"
    elif invite.status == invite.STATUS_JOINED_INDEPENDENTLY:
        return "joined"
    return ""
