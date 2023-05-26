from django import forms


class Add_Password(forms.Form):
    userName = forms.CharField(label="UserName:", max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control text-dark'}))
    userPass = forms.CharField(label="Password", max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control text-dark', 'type': 'password'}))
    desc = forms.CharField(label="Description", max_length=100,
                           widget=forms.TextInput(attrs={'class': 'form-control text-dark'}))
