from django import forms


class AddTask(forms.Form):
    title = forms.CharField(label="", max_length=255,
                            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'new task...'}))
