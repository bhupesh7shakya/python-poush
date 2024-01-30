from django.shortcuts import render, redirect
from .models import *
from .forms import *

def get_task(pk = None, all = False):
    if all:
        return Task.objects.all()
    else:
        return Task.objects.get(pk = pk)

# Create your views here.
def home(request):
    search_result = SearchBox(request.GET)
    if search_result.is_valid():
        search_mode = True
        search_term = search_result.cleaned_data['term']
        task = Task.objects.filter(description = search_term).all() 
        context = {
            'search': search_mode,
            'search_form': SearchBox(),
            'data': task
        }
        return render(request, 'home.html', context)
    else:
        search_mode = False
        task = get_task(all = True)
        task_count = {
            'total_task': task.count(),
            'total_completed': task.filter(status = True).count(),
            'total_incomplete': task.filter(status = False).count()
        }
        context = {
            'search': search_mode,
            'search_form': SearchBox(),
            'data': task,
            'task_status': task_count
        }
        return render(request, 'home.html', context)

def delete(request, id):
    task = get_task(pk=id)
    task.delete()
    return redirect("/")

def change(request, id):
    task = get_task(pk = id)
    task.status = True if task.status == False else False
    task.save()
    return redirect("/")

def insert(request):
    if request.method == "GET":
        context = {
            'edit': False,
            'form': TaskForm
        }
        return render(request, 'insert.html', context)
    else:
        data = TaskForm(request.POST)
        if data.is_valid():
            task = Task(title=data.cleaned_data['title'].strip(), description = data.cleaned_data['description'].strip(), status = data.cleaned_data['status'] if data.cleaned_data['status'] != None else False)
            task.save()
            return redirect('/')
    
def edit(request, id = None):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = Task.objects.filter(pk=id).update(title = form.cleaned_data['title'], description = form.cleaned_data['description'], status = form.cleaned_data['status'])
            return redirect('/')
    else:
        task = get_task(id)
        form = TaskForm(initial={'title': task.title, 'description': task.description, 'status' : task.status})
        context = {
            'search_form': SearchBox(),
            'edit': True,
            'form': form
        }
        return render(request, 'insert.html', context)