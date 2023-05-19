from django import forms


class register_forms(forms.Form):
    userName = forms.CharField(label="Name:", max_length=250, widget=forms.TextInput(
        attrs={'class': 'form-control text-dark'}))
    userEmail = forms.CharField(label="Email:", max_length=250, widget=forms.TextInput(
        attrs={'class': 'form-control text-dark'}))
    userPass = forms.CharField(label="Password", max_length=250, widget=forms.TextInput(
        attrs={'class': 'form-control text-dark', 'type': 'password'}))
    confPass = forms.CharField(label="Confirm Password", max_length=250, widget=forms.TextInput(
        attrs={'class': 'form-control text-dark', 'type': 'password'}))


class login_form(forms.Form):
    userEmail = forms.CharField(label="Email:", max_length=250, widget=forms.TextInput(
        attrs={'class': 'form-control text-dark'}))
    userPass = forms.CharField(label="Password", max_length=250, widget=forms.TextInput(
        attrs={'class': 'form-control text-dark', 'type': 'password'}))
