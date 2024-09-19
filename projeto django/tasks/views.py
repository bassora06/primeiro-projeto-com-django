from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm
from django.core.paginator import Paginator
from django.contrib import messages
# Create your views here.

def taskList(request):
    tasks_list = Task.objects.all().order_by('-created_at')

    paginator = Paginator(tasks_list, 5)

    page = request.GET.get('page')

    tasks = paginator.get_page(page)

    return render(request, 'tasks/list.html', {'tasks' : tasks})

def helloWorld(request):
    return HttpResponse('Tasks')


def newTask(request): 
    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            task.done = 'doing'
            task.save()
            messages.info(request, 'Tarefa adicionada com sucesso')
            return redirect('/')

    else:
        form = TaskForm()
        return render(request, 'tasks/newTask.html', {'form': form})


def taskView(request, id):
    task = get_object_or_404(Task, pk=id)
    return render(request, 'tasks/task.html', {'task': task})


def editTask(request, id):
    task = get_object_or_404(Task, pk=id)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)

        if form.is_valid():
            task.save()
            messages.info(request, 'Tarefa editada com sucesso')
            return redirect('/')
        else:
            return render(request, 'tasks/editTask.html', {'form': form, 'task': task})
    else:
        return render(request, 'tasks/editTask.html', {'form': form, 'task': task})
    

def deleteTask(request, id):
    task = get_object_or_404(Task, pk=id)
    task.delete()
    messages.info(request, 'Tarefa deletada com sucesso')
    return redirect('/')


