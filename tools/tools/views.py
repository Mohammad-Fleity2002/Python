from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


# #@login_required(login_url="/")
def home(request):
    return render(request, 'home.html')


def handler404(request, *args, **kwargs):
    return redirect('/login/')
