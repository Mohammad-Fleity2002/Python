from django.shortcuts import render


def home(request, user_id):
    return render(request, 'home.html')
