from django import forms


class Add_Contact(forms.Form):
    full_name = forms.CharField(label="Full Name:", max_length=255, widget=forms.TextInput(
        attrs={'class': 'form-control text-dark'}))
    phone_number = forms.CharField(label="Phone Number", max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control text-dark', 'type': 'tel'}))
    desc = forms.CharField(label="Description", max_length=255,
                           widget=forms.TextInput(attrs={'class': 'form-control text-dark'}))
