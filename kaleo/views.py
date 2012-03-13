from django import http
from django.utils import simplejson as json
from django.views.decorators.http import require_http_methods

from django.contrib.auth.decorators import login_required

from account.models import EmailAddress
from kaleo.forms import InviteForm
from kaleo.models import JoinInvitation


@login_required
@require_http_methods(["POST"])
def invite(request):
    form = InviteForm(request.POST)
    if form.is_valid():
        email = form.cleaned_data["email_address"]
        if EmailAddress.objects.filter(email=email, verified=True).exists():
            data = {"status": "ERROR", "errors": '<ul class="errorlist"><li>%s is already on this site</li></ul>' % email}
        elif JoinInvitation.objects.filter(from_user=request.user, signup_code__email=email).exists():
            data = {"status": "ERROR", "errors": '<ul class="errorlist"><li>You have already invited %s</li></ul>' % email}
        else:
            JoinInvitation.invite(request.user, email)
            data = {
                "status": "OK",
                "email": email,
                "invitations_remaining": request.user.invitationstat.invites_remaining()
            }
    else:
        data = {"status": "ERROR", "errors": str(form.errors["email_address"])}
    return http.HttpResponse(json.dumps(data), content_type="application/json")
