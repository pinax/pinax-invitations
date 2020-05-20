from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import permission_required
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.template import RequestContext
from django.template.loader import render_to_string
from django.utils.decorators import method_decorator
from django.views.generic import View
from django.views.generic.edit import FormMixin

from account.mixins import LoginRequiredMixin

from .forms import InviteForm
from .models import InvitationStat, JoinInvitation


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
                }, request=self.request
            ),
            "fragments": {
                self.invites_remaining_fragment_selector: render_to_string(
                    self.invites_remaining_fragment, {
                        "invites_remaining": self.request.user.invitationstat.invites_remaining()
                    }, request=self.request
                ),
                self.invited_fragment_selector: render_to_string(
                    self.invited_fragment, {
                        "invited_list": self.request.user.invites_sent.all()
                    }, request=self.request
                )
            }
        }
        return data

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
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


class ManageInvitesView(LoginRequiredMixin, View):

    @method_decorator(permission_required("pinax-invitations.manage_invites", raise_exception=True))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class InviteStatView(ManageInvitesView):

    def get(self, request, *args, **kwargs):
        user = get_object_or_404(get_user_model(), pk=kwargs.get("pk"))
        return JsonResponse({
            "html": render_to_string(
                self.invite_stat_fragment, {
                    "stat": user.invitationstat
                }, context_instance=RequestContext(request)
            )
        })


class ManageInviteAmountsView(ManageInvitesView):
    amount_post_var = "amount"

    def get_amount(self):
        return int(self.request.POST.get(self.amount_post_var))


class AllManageInviteAmountsView(ManageInviteAmountsView):

    def action(self, amount):
        return

    def post(self, request, *args, **kwargs):
        amount = self.get_amount()
        self.action(amount)
        return JsonResponse({
            "inner-fragments": {self.inner_fragments_amount_selector: amount}
        })


class UserManageInviteAmountsView(ManageInviteAmountsView):

    def action(self, user, amount):
        return

    def post(self, request, *args, **kwargs):
        user = get_object_or_404(get_user_model(), pk=kwargs.get("pk"))
        amount = self.get_amount()
        self.action(user, amount)
        return JsonResponse({
            "html": amount
        })


class TopOffAllView(AllManageInviteAmountsView):

    inner_fragments_amount_selector = ".invite-total"

    def action(self, amount):
        InvitationStat.topoff(amount)


class TopOffUserView(UserManageInviteAmountsView):

    def action(self, user, amount):
        InvitationStat.topoff_user(user=user, amount=amount)


class AddToAllView(AllManageInviteAmountsView):

    inner_fragments_amount_selector = ".amount-added"

    def action(self, amount):
        InvitationStat.add_invites(amount)


class AddToUserView(UserManageInviteAmountsView):

    def action(self, user, amount):
        InvitationStat.add_invites_to_user(user=user, amount=amount)
