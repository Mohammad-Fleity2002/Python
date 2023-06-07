from django import forms


class Add_Password(forms.Form):
    userName = forms.CharField(label="User Name:", max_length=100, min_length=10, widget=forms.TextInput(
        attrs={'class': 'form-control text-dark'}))
    userPass = forms.CharField(widget=forms.PasswordInput(
        attrs={"class": "form-control text-dark"}), label="Password", min_length=8)
    desc = forms.CharField(label="Description", max_length=100, min_length=8,
                           widget=forms.TextInput(attrs={'class': 'form-control text-dark'}))
