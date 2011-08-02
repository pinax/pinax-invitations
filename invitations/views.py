from django import http
from django.utils import simplejson as json
from django.views.decorators.http import require_http_methods

from django.contrib.auth.decorators import login_required

from emailconfirmation.models import EmailAddress

from invitations.forms import InviteForm
from invitations.models import JoinInvitation


@login_required
@require_http_methods(["POST"])
def invite(request):
    form = InviteForm(request.POST)
    if form.is_valid():
        email = form.cleaned_data["email_address"]
        if EmailAddress.objects.filter(email=email, verified=True).exists():
            data = {"status": "ERROR", "errors": "A user with %s as their email address already exists." % email}
        else:
            JoinInvitation.invite(request.user, email)
            data = {
                "status": "OK",
                "email": email,
                "invitations_remaining": request.user.invitationstat.invites_remaining()
            }
    else:
        data = {"status": "ERROR", "errors": form.errors}
    return http.HttpResponse(json.dumps(data), content_type="application/json")
