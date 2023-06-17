from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import LoginForm, signForm, changePassForm
from django.views.decorators.cache import never_cache
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth import views as auth_view


@never_cache
def login_user(request):
    # patch_cache_control(response, private=True)
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == "POST":
        loginform = LoginForm(request.POST)
        if loginform.is_valid():
            username = request.POST['userName']
            password = request.POST['userPass']
            user = login_authenticate(
                username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.success(request, ("There was an Error logging in"))
    else:
        loginform = LoginForm()
    return render(request, 'Registration/login.html', {"form": loginform})


def logout_user(request):
    logout(request)
    messages.success(request, ("Logged OUt Successfully"))
    return redirect("/login/")


def sign_up(request):
    if request.user.is_authenticated:
        return redirect('/')
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
            return redirect('/')
    else:
        signUpForm = signForm()
    return render(request, 'Registration/sign_up.html', {'form': signUpForm})


def login_authenticate(username=None, password=None):
    try:
        user = User.objects.get(
            Q(username__iexact=username))
        if user != None and user.check_password(password):
            return user
        else:
            raise User.DoesNotExist
    except User.DoesNotExist:
        user = None
    return user


def change_pass(request):
    if request.method == "POST":
        myForm = changePassForm(request.POST)
        if myForm.is_valid():
            email = myForm.cleaned_data['email']
            password1 = myForm.cleaned_data['password1']
            # password2 = myForm.cleaned_data['password2']
            try:
                user = User.objects.get(email=email)
                user.set_password(password1)
                user.save()
                messages.success(
                    request, ("password changed successfully"))
                return redirect('/login/')
            except User.DoesNotExist:
                messages.error(
                    request, ("no email found, try to sign up."))
    else:
        myForm = changePassForm()
    return render(request, 'Registration/change_password.html', {'form': myForm})
