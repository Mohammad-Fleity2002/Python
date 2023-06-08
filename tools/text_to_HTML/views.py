from django.shortcuts import render
from .forms import EditorForm
from django.contrib.auth.decorators import login_required


@login_required(login_url="/")
def index(request):
    form = EditorForm()
    return render(request, 'text_to_HTML/index.html', {'form': form})
