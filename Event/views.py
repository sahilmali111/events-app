from django.shortcuts import render, redirect
from .forms import *
import pyodbc


# Create your views here.
def index(request):
    result = addevent.objects.all()
    return render(request, 'index.html', {'result': result})


def add_event(request):
    if request.method == "POST":
        form = eventform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            print(form.errors)
    return render(request, 'addevent.html')


def like_event(request):
    eid = request.GET.get('eid', None)
    addevent.objects.filter(id=eid).update(islike=1)
    return redirect('/')

def dislike_event(request):
    eid = request.GET.get('eid', None)
    addevent.objects.filter(id=eid).update(islike=0)
    return redirect('/')
