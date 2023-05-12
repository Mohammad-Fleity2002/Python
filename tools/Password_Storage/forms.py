
from django import forms
non_allowed_usernames = ['abc']


class AddPass(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            "class": "form-control",
            "id": "username"
        }))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "id": "user-password"
            }
        )
    )
    description = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "desc"
            }
        )
    )
