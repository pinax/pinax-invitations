import json

from django.contrib.auth import get_user_model
from django.http import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404
from django.template import RequestContext
from django.template.loader import render_to_string
from django.views.decorators.http import require_POST
from django.views.generic import FormMixin, View
from django.contrib.auth.decorators import permission_required

from account.decorators import login_required
from account.mixins import LoginRequiredMixin

from .forms import InviteForm
from .models import JoinInvitation, InvitationStat


class InviteView(LoginRequiredMixin, FormMixin, View):

    form_class = InviteForm
    invite_form_fragment = "pinax/invitations/_invite_form.html"
    invites_remaining_fragment = "pinax/invitations/_invites_remaining.html"
    invited_fragment = "pinax/invitations/_invited.html"
    invites_remaining_fragment_selector = ".pinax-invitations-invites-remaining"
    invited_fragment_selector = ".pinax-invitations-invites-sent"

    def get_data(self, form):
        data = {
            "html": render_to_string(
                self.invite_form_fragment, {
                    "form": form,
                    "user": self.request.user
                }, context_instance=RequestContext(self.request)
            ),
            "fragments": {
                self.invites_remaining_fragment_selector: render_to_string(
                    self.invites_remaining_fragment, {
                        "invites_remaining": self.request.user.invitationstat.invites_remaining()
                    }, context_instance=RequestContext(self.request)
                ),
                self.invited_fragment_selector: render_to_string(
                    self.invited_fragment, {
                        "invited_list": self.request.user.invites_sent.all()
                    }, context_instance=RequestContext(self.request)
                )
            }
        }
        return data

    def get_form_kwargs(self):
        kwargs = super(InviteView, self).get_form_kwargs()
        kwargs.update({
            "user": self.request.user
        })
        return kwargs

    def form_valid(self, form):
        email = form.cleaned_data["email_address"]
        JoinInvitation.invite(self.request.user, email)
        return JsonResponse(self.get_data(InviteForm(user=self.request.user)))

    def form_invalid(self, form):
        return JsonResponse(self.get_data(form))

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


@login_required
@permission_required("pinax-invitations.manage_invites", raise_exception=True)
def invite_stat(request, pk):
    user = get_object_or_404(get_user_model(), pk=pk)
    return HttpResponse(json.dumps({
        "html": render_to_string(
            "pinax/invitations/_invite_stat.html", {
                "stat": user.invitationstat
            }, context_instance=RequestContext(request)
        )
    }), content_type="application/json")


@login_required
@permission_required("pinax-invitations.manage_invites", raise_exception=True)
@require_POST
def topoff_all(request):
    amount = int(request.POST.get("amount"))
    InvitationStat.topoff(amount)
    return HttpResponse(json.dumps({
        "inner-fragments": {".invite-total": amount}
    }), content_type="application/json")


@login_required
@permission_required("pinax-invitations.manage_invites", raise_exception=True)
@require_POST
def topoff_user(request, pk):
    user = get_object_or_404(get_user_model(), pk=pk)
    amount = int(request.POST.get("amount"))
    InvitationStat.topoff_user(user=user, amount=amount)
    return HttpResponse(json.dumps({
        "html": amount
    }), content_type="application/json")


@login_required
@permission_required("pinax-invitations.manage_invites", raise_exception=True)
@require_POST
def addto_all(request):
    amount = int(request.POST.get("amount"))
    InvitationStat.add_invites(amount)
    return HttpResponse(json.dumps({
        "inner-fragments": {".amount-added": amount}
    }), content_type="application/json")


@login_required
@permission_required("pinax-invitations.manage_invites", raise_exception=True)
@require_POST
def addto_user(request, pk):
    user = get_object_or_404(get_user_model(), pk=pk)
    amount = int(request.POST.get("amount"))
    InvitationStat.add_invites_to_user(user=user, amount=amount)
    return HttpResponse(json.dumps({
        "html": amount
    }), content_type="application/json")
