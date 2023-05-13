from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect
from .models import Passwords
from .forms import Add_Password
# Create your views here.


def index(request):
    passwords = Passwords.objects.all()
    return render(request, 'Password_Storage/index.html', {'passwords': passwords})


def AddPassword(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        myform = Add_Password(request.POST)
        # check whether it's valid:
        if myform.is_valid():
            # process the data in form.cleaned_data as required
            # redirect to a new URL:
            userName = myform.cleaned_data["userName"]
            Pass = myform.cleaned_data["userPass"]
            userdesc = myform.cleaned_data["desc"]
            newPass = Passwords(username=userName,
                                password=Pass, description=userdesc)
            newPass.save()
            return index(request=None)

    # if a GET (or any other method) we'll create a blank form
    else:
        myform = Add_Password()

    return render(request, "Password_Storage/Add_Password.html", {"form": myform})
