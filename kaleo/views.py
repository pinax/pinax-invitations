import json

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.template import RequestContext
from django.template.loader import render_to_string
from django.views.decorators.http import require_POST

from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required

from kaleo.compat import get_user_model
from kaleo.forms import InviteForm
from kaleo.models import JoinInvitation, InvitationStat


@login_required
@require_POST
def invite(request):
    form = InviteForm(request.POST, user=request.user)
    if form.is_valid():
        email = form.cleaned_data["email_address"]
        JoinInvitation.invite(request.user, email)
        form = InviteForm(user=request.user)
    data = {
        "html": render_to_string(
            "kaleo/_invite_form.html", {
                "form": form,
                "user": request.user
            }, context_instance=RequestContext(request)
        ),
        "fragments": {
            ".kaleo-invites-remaining": render_to_string(
                "kaleo/_invites_remaining.html", {
                    "invites_remaining": request.user.invitationstat.invites_remaining()
                }, context_instance=RequestContext(request)
            ),
            ".kaleo-invites-sent": render_to_string(
                "kaleo/_invited.html", {
                    "invited_list": request.user.invites_sent.all()
                }, context_instance=RequestContext(request)
            )
        }
    }
    return HttpResponse(json.dumps(data), content_type="application/json")


@login_required
@permission_required("kaleo.manage_invites", raise_exception=True)
def invite_stat(request, pk):
    user = get_object_or_404(get_user_model(), pk=pk)
    return HttpResponse(json.dumps({
        "html": render_to_string(
            "kaleo/_invite_stat.html", {
                "stat": user.invitationstat
            }, context_instance=RequestContext(request)
        )
    }), content_type="application/json")


@login_required
@permission_required("kaleo.manage_invites", raise_exception=True)
@require_POST
def topoff_all(request):
    amount = int(request.POST.get("amount"))
    InvitationStat.topoff(amount)
    return HttpResponse(json.dumps({
        "inner-fragments": {".invite-total": amount}
    }), content_type="application/json")


@login_required
@permission_required("kaleo.manage_invites", raise_exception=True)
@require_POST
def topoff_user(request, pk):
    user = get_object_or_404(get_user_model(), pk=pk)
    amount = int(request.POST.get("amount"))
    InvitationStat.topoff_user(user=user, amount=amount)
    return HttpResponse(json.dumps({
        "html": amount
    }), content_type="application/json")


@login_required
@permission_required("kaleo.manage_invites", raise_exception=True)
@require_POST
def addto_all(request):
    amount = int(request.POST.get("amount"))
    InvitationStat.add_invites(amount)
    return HttpResponse(json.dumps({
        "inner-fragments": {".amount-added": amount}
    }), content_type="application/json")


@login_required
@permission_required("kaleo.manage_invites", raise_exception=True)
@require_POST
def addto_user(request, pk):
    user = get_object_or_404(get_user_model(), pk=pk)
    amount = int(request.POST.get("amount"))
    InvitationStat.add_invites_to_user(user=user, amount=amount)
    return HttpResponse(json.dumps({
        "html": amount
    }), content_type="application/json")
