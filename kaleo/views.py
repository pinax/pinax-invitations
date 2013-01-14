import json

from django import http
from django.template import RequestContext
from django.template.loader import render_to_string
from django.views.decorators.http import require_POST

from django.contrib.auth.decorators import login_required

from kaleo.forms import InviteForm
from kaleo.models import JoinInvitation


@login_required
@require_POST
def invite(request):
    form = InviteForm(request.POST, user=request.user)
    if form.is_valid():
        email = form.cleaned_data["email_address"]
        JoinInvitation.invite(request.user, email)
        form = InviteForm(user=request.user)
    data = {
        "html": render_to_string("kaleo/_invite_form.html", {
                "form": form,
                "user": request.user
            }, context_instance=RequestContext(request)
        ),
        "fragments": {
            ".kaleo-invites-remaining": render_to_string("kaleo/_invites_remaining.html", {
                    "invites_remaining": request.user.invitationstat.invites_remaining()
                }, context_instance=RequestContext(request)
            ),
            ".kaleo-invites-sent": render_to_string("kaleo/_invited.html", {
                    "invited_list": request.user.invites_sent.all()
                }, context_instance=RequestContext(request)
            )
        }
    }
    return http.HttpResponse(json.dumps(data), content_type="application/json")
