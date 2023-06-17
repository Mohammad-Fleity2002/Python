from django.shortcuts import render, redirect
from .models import Passwords
from .forms import Add_Password
from django.contrib.auth.decorators import login_required


# #@login_required(login_url="/")
def index(request):
    passwords = Passwords.objects.all()
    return render(request, 'Password_Storage/index.html', {'passwords': passwords})


# @login_required(login_url="/")
def AddPassword(request):
    if request.method == "POST":
        myform = Add_Password(request.POST)
        if myform.is_valid():
            myform.save()
            return redirect('/Password_Storage/')
    else:
        myform = Add_Password()
    return render(request, "Password_Storage/Add_Password.html", {"form": myform})


# @login_required(login_url="/")
def deletePassword(request, item_id):
    item = Passwords.objects.get(id=item_id)
    item.delete()
    return redirect(request.META.get('HTTP_REFERER'))
