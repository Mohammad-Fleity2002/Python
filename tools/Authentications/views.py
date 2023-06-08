from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import LoginForm, signForm


def login_user(request):
    if request.user.is_authenticated:
        return redirect('/home/')
    if request.method == "POST":
        loginform = LoginForm(request.POST)
        if loginform.is_valid():
            username = request.POST['userName']
            password = request.POST['userPass']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/home/')
            else:
                messages.success(request, ("There was an Error logging in"))
    else:
        loginform = LoginForm()
    return render(request, 'Registration/login.html', {"form": loginform})


def logout_user(request):
    logout(request)
    messages.success(request, ("Logged OUt Successfully"))
    return redirect("/")


def sign_up(request):
    if request.user.is_authenticated:
        return redirect('/home/')
    if request.method == "POST":
        signUpForm = signForm(request.POST)
        if signUpForm.is_valid():
            signUpForm.save()
            username = signUpForm.cleaned_data['username']
            fname = signUpForm.cleaned_data['first_name']
            lname = signUpForm.cleaned_data['last_name']
            password = signUpForm.cleaned_data['password1']
            user = authenticate(
                username=username, password=password, first_name=fname, last_name=lname)
            login(request, user)
            messages.success(
                request, ("Success!!! Thanks for creating an account in out tool app!"))
            return redirect('/home/')
    else:
        signUpForm = signForm()
    return render(request, 'Registration/sign_up.html', {'form': signUpForm})
