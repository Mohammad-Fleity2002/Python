from django.shortcuts import render, redirect
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


def deletTask(request, item_id):
    item = task.objects.get(id=item_id)
    item.delete()
    return redirect(request.META.get('HTTP_REFERER'))


def checkTask(request, item_id):
    item = task.objects.get(id=item_id)
    if item.cheked:
        item.cheked = False
    else:
        item.cheked = True
    item.save()
    return redirect(request.META.get('HTTP_REFERER'))


def allTask(request):
    tasks = task.objects.all()
    return render(request, "TO_DO/all_task.html", {'tasks': tasks})
