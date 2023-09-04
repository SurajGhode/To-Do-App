from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm

def task_list(request):
    tasks = Task.objects.filter(completed__isnull=True)  # Get tasks that are not completed
    completed_tasks = Task.objects.filter(completed__isnull=False)  # Get completed tasks

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')

    else:
        form = TaskForm()

    return render(request, 'tasks/task_list.html', {'tasks': tasks, 'completed_tasks': completed_tasks, 'form': form})

def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('task_list')

def complete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.completed = not task.completed
    task.save()
    return redirect('task_list')

def set_reminder(request, pk):
    task = get_object_or_404(Task, pk=pk)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')

    else:
        form = TaskForm(instance=task)

    return render(request, 'tasks/set_reminder.html', {'form': form, 'task': task})