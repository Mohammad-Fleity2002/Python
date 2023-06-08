from django.shortcuts import render,  redirect
from django.contrib.auth.decorators import login_required
from .models import Contacts
from .forms import Add_Contact


@login_required(login_url="/")
def index(request):
    contacts = Contacts.objects.all()
    return render(request, 'My_Contact/index.html', {'Contacts': contacts})


@login_required(login_url="/")
def AddContact(request):
    if request.method == "POST":
        myform = Add_Contact(request.POST)
        if myform.is_valid():
            myform.save()
            return redirect('/My_Contact/')
    else:
        myform = Add_Contact()
    return render(request, "My_Contact/Add_Contact.html", {"form": myform})


@login_required(login_url="/")
def deleteContact(request, item_id):
    cntct = Contacts.objects.get(id=item_id)
    cntct.delete()
    return redirect(request.META.get('HTTP_REFERER'))
