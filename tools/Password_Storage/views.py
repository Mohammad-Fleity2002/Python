from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect
from .models import Passwords
from django.contrib import messages
from django.db.models import Q
from .forms import *
# Create your views here.


def index(request):
    passwords = Passwords.objects.all()
    return render(request, 'Password_Storage/index.html', {'passwords': passwords})


def Add_Password(request):
    # Use the AddPass form from forms.py
    form = AddPass(request.POST or None)
    # check if valid if so create a Password otherwise raise an exeption
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("user-password")
        desc = form.cleaned_data.get("desc")
        try:
            new_Password = Passwords.objects.create(username, password, desc)
        except:
            new_Password = None
    return render(request, "Password_Storage/Add_Password.html", {"form": form})
