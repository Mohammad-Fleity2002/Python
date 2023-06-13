from django import forms
from .models import Passwords
from django.contrib.auth.password_validation import validate_password
from django.core import validators


class Add_Password(forms.ModelForm):
    class Meta:
        model = Passwords
        fields = {"username", "password", "description"}

        def save(self, commit=True):
            password = super.save(commit=False)
            if commit:
                password.save()
            return password

    def __init__(self, *args: any, **kwargs: any) -> None:
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].label = 'User Name'
        self.fields['username'].widget.attrs['min'] = 8
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].label = 'Password'
        self.fields['password'].validators = [validate_password]
        self.fields['description'].widget.attrs['class'] = 'form-control'
        self.fields['description'].label = 'Description'

    # userName = forms.CharField(label="User Name:", max_length=100, min_length=10, widget=forms.TextInput(
    #     attrs={'class': 'form-control text-dark'}))
    # userPass = forms.CharField(widget=forms.PasswordInput(
    #     attrs={"class": "form-control text-dark"}), label="Password", min_length=8, validators=[validate_password])
    # desc = forms.CharField(label="Description", max_length=100, min_length=8,
    #                        widget=forms.TextInput(attrs={'class': 'form-control text-dark'}))
