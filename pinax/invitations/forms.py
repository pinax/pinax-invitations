from django import forms
from django.utils.translation import ugettext as _

from account.models import EmailAddress

from .models import JoinInvitation


class InviteForm(forms.Form):
    email_address = forms.EmailField()

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user")
        super(InviteForm, self).__init__(*args, **kwargs)

    def clean_email_address(self):
        email = self.cleaned_data["email_address"]
        if EmailAddress.objects.filter(email=email, verified=True).exists():
            raise forms.ValidationError(_("Email address already in use"))
        elif JoinInvitation.objects.filter(from_user=self.user, signup_code__email=email).exists():
            raise forms.ValidationError(_("You have already invited this user"))
        return email
