from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from .models import task
from .forms import AddTask
from datetime import datetime
# from django.utils import timezone

# Create your views here.


def index(request):
    # Entry.objects.all().filter(pub_date__year=2006)
    tasks = task.objects.all().filter(add_date=datetime.today())
    if request.method == "POST":
        form = AddTask(request.POST)
        if form.is_valid():
            n = form.cleaned_data["title"]
            t = task(title=n)
            t.save()
    else:
        form = AddTask()
    return render(request, "TO_DO/index.html", {'form': form, 'tasks': tasks})
