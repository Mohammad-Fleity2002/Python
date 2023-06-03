from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    userName = forms.CharField(label="User Name:", max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control text-dark'}))
    userPass = forms.CharField(label="Password", max_length=100, widget=forms.PasswordInput(
        attrs={'class': 'form-control text-dark', 'type': 'password'}))


class signForm(UserCreationForm):
    email = forms.EmailField(label="Email:", max_length=200, widget=forms.EmailInput(
        attrs={'class': 'form-control text-dark'})
    )
    firstName = forms.CharField(label="First Name:", max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control text-dark'})
    )
    lastName = forms.CharField(label="Last Name:", max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control text-dark'})
    )

    class Meta:
        model = User
        fields = ('username', 'firstName', 'lastName',
                  'email', 'password1', 'password2')
    # redesignind default inputs of django

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].label = 'User Name'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
