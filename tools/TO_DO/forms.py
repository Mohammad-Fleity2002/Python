from django import forms

# create a form as a class


class AddTask(forms.Form):
    title = forms.CharField(label="", max_length=255,
                            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'new task...'}))
    # by default all fields required you should add:
    # title = forms.CharField(label="task title", max_length=255,required=False)
    #     firstname= forms.CharField(max_length=100,
    #            widget= forms.TextInput
    #            (attrs={'class':'some_class',
    #    'id':'some_id'}))
