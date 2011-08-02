from django.contrib import admin

from invitations.models import JoinInvitation, InvitationStat


class InvitationStatAdmin(admin.ModelAdmin):
    readonly_fields = ["user", "invites_sent", "invites_accepted"]
    list_display = ["user", "invites_sent", "invites_accepted", "invites_allocated", "invites_remaining", "can_send"]
    list_filter = ["invites_sent", "invites_accepted"]


admin.site.register(JoinInvitation)
admin.site.register(InvitationStat, InvitationStatAdmin)
