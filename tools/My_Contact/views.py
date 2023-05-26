from django.shortcuts import render,  redirect
from .models import Contacts
from .forms import Add_Contact


def index(request):
    contacts = Contacts.objects.all()
    return render(request, 'My_Contact/index.html', {'Contacts': contacts})


def AddContact(request):
    if request.method == "POST":
        myform = Add_Contact(request.POST)
        if myform.is_valid():
            full_name = myform.cleaned_data["full_name"]
            phone_number = myform.cleaned_data["phone_number"]
            userdesc = myform.cleaned_data["desc"]
            newContact = Contacts(full_name=full_name,
                                  phone_number=phone_number, description=userdesc)
            newContact.save()
            return redirect('/My_Contact/')
    else:
        myform = Add_Contact()
    return render(request, "My_Contact/Add_Contact.html", {"form": myform})


def deleteContact(request, item_id):
    cntct = Contacts.objects.get(id=item_id)
    cntct.delete()
    return redirect(request.META.get('HTTP_REFERER'))
