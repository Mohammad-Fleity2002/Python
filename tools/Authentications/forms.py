from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm, PasswordChangeForm
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    userName = forms.CharField(label="User Name:", max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control text-dark'}))
    userPass = forms.CharField(label="Password", max_length=100, widget=forms.PasswordInput(
        attrs={'class': 'form-control text-dark', 'type': 'password'}))


class signForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2')

        def save(self, commit=True):
            User = super.save(commit=False)
            if commit:
                User.save()
            return User
    # redesignind default inputs of django

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].label = 'User Name'
        self.fields['username'].unique = 'True'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'


class changePassForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')

        # def save(self, commit=True):
        #     User = super.save(commit=False)
        #     if commit:
        #         User.save()
        #     return User

        # redesignind default inputs of django

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
