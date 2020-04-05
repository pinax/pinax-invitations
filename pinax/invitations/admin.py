from django.contrib import admin
from django.contrib.auth import get_user_model

from .models import InvitationStat, JoinInvitation

User = get_user_model()


class InvitationStatAdmin(admin.ModelAdmin):
    raw_id_fields = ["user"]
    readonly_fields = ["invites_sent", "invites_accepted"]
    list_display = [
        "user",
        "invites_sent",
        "invites_accepted",
        "invites_allocated",
        "invites_remaining",
        "can_send"
    ]
    list_filter = ["invites_sent", "invites_accepted"]


admin.site.register(
    JoinInvitation,
    list_display=["from_user", "to_user", "sent", "status", "to_user_email"],
    list_filter=["sent", "status"],
    search_fields=[f"from_user__{User.USERNAME_FIELD}"]
)
admin.site.register(InvitationStat, InvitationStatAdmin)
