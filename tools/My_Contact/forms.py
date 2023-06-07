from django import forms
from .models import Contacts


class Add_Contact(forms.ModelForm):
    class Meta:
        model = Contacts
        fields = {"full_name", "phone_number", "description"}

        def save(self, commit=True):
            contact = super.save(commit=False)
            if commit:
                contact.save()
            return contact

    def __init__(self, *args: any, **kwargs: any) -> None:
        super().__init__(*args, **kwargs)
        self.fields['full_name'].widget.attrs['class'] = 'form-control'
        self.fields['phone_number'].widget.attrs['class'] = 'form-control'
        self.fields['description'].widget.attrs['class'] = 'form-control'

    # full_name = forms.CharField(label="Full Name:", max_length=255, min_length=10, widget=forms.TextInput(
    #     attrs={'class': 'form-control text-dark'}))
    # phone_number = forms.CharField(label="Phone Number", max_length=100, min_length=8, widget=forms.TextInput(
    #     attrs={'class': 'form-control text-dark', 'type': 'tel'}))
    # desc = forms.CharField(label="Description", max_length=255,
    #                        widget=forms.TextInput(attrs={'class': 'form-control text-dark'}))
