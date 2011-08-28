from django import forms


class InviteForm(forms.Form):
    
    email_address = forms.EmailField()
