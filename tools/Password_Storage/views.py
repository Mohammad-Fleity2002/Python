from django.shortcuts import render, redirect
from .models import Passwords
from .forms import Add_Password


def index(request):
    passwords = Passwords.objects.all()
    return render(request, 'Password_Storage/index.html', {'passwords': passwords})


def AddPassword(request):
    if request.method == "POST":
        myform = Add_Password(request.POST)
        if myform.is_valid():
            userName = myform.cleaned_data["userName"]
            Pass = myform.cleaned_data["userPass"]
            userdesc = myform.cleaned_data["desc"]
            newPass = Passwords(username=userName,
                                password=Pass, description=userdesc)
            newPass.save()
            return redirect('/Password_Storage/')
    else:
        myform = Add_Password()
    return render(request, "Password_Storage/Add_Password.html", {"form": myform})


def deletePassword(request, item_id):
    item = Passwords.objects.get(id=item_id)
    item.delete()
    return redirect(request.META.get('HTTP_REFERER'))
