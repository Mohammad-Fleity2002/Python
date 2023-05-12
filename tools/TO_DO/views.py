from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from .models import task
# Create your views here.


def index(request):
    tasks = task.objects.all()
    return render(request, 'TO_DO/index.html', {'tasks': tasks})
