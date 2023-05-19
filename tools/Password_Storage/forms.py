from django import forms


class Add_Password(forms.Form):
    userName = forms.CharField(label="UserName:", max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control text-dark'}))
    userPass = forms.CharField(label="Password", max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control text-dark', 'type': 'password'}))
    desc = forms.CharField(label="Description", max_length=100,
                           widget=forms.TextInput(attrs={'class': 'form-control text-dark'}))


# class Edit_Password(forms.Form):
#     userName = forms.CharField(label="New UserName:", max_length=100, widget=forms.TextInput(
#         attrs={'class': 'form-control text-dark'}), required=False)
#     userPass = forms.CharField(label="New Password", max_length=100, widget=forms.TextInput(
#         attrs={'class': 'form-control text-dark', 'type': 'password'}), required=False)
#     desc = forms.CharField(label=" New Description", max_length=100,
#                            widget=forms.TextInput(attrs={'class': 'form-control text-dark'}), required=False)
