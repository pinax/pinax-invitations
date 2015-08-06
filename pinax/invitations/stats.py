from .models import JoinInvitation


def stats():
    return {
        "join_invitations_sent": JoinInvitation.objects.count(),
        "join_invitations_accepted": JoinInvitation.objects.filter(
            status=JoinInvitation.STATUS_ACCEPTED
        ).count()
    }
