from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from .forms import login_form, register_forms
from .models import Users
# Create your views here.


def login(request):
    if request.method == "POST":
        myform = login_form(request.POST)
        if myform.is_valid():
            email = myform.cleaned_data["userEmail"]
            Pass = myform.cleaned_data["userPass"]
            try:
                user = Users.objects.get(user_email=email, user_password=Pass)
                return redirect(f'{user.id}/')
            except Exception:
                message = "Wrong Cridentials"
                return render(request, 'Authentication/Error.html', {'message': message})
    else:
        myform = login_form()
    return render(request, "Authentication/Login.html", {"form": myform})


def register(request):
    if request.method == "POST":
        myform = register_forms(request.POST)
        if myform.is_valid():
            name = myform.cleaned_data["userName"]
            email = myform.cleaned_data["userEmail"]
            Pass = myform.cleaned_data["userPass"]
            confPass = myform.cleaned_data["confPass"]
            if Pass == confPass:
                try:
                    is_new = Users.objects.get(user_email=email)
                    # if is_new:#no need try except is enough
                    message = "Email already exist"
                    return render(request, 'Authentication/Error.html', {'message': message})
                except Exception:
                    newUser = Users(
                        user_name=name, user_email=email, user_password=Pass)
                    newUser.save()
                    return redirect("/")
            else:
                message = "Password doesn't matches"
                return render(request, 'Authentication/Error.html', {'message': message})
            # return index(request=None)
    else:
        myform = register_forms()
    return render(request, "Authentication/register.html", {"form": myform})
    # return render(request, "/Login.html")
