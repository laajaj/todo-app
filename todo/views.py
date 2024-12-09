
from django.shortcuts import render
from .models import Task

def task_list(request):
    tasks = Task.objects.all().order_by('-created_at')
    return render(request, 'todo/task_list.html', {'tasks': tasks})

from django.shortcuts import render, redirect
from .forms import TaskForm

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'todo/add_task.html', {'form': form})

from django.shortcuts import get_object_or_404, redirect
from .models import Task

def mark_as_completed(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.is_completed = True
    task.save()
    return redirect('task_list')
