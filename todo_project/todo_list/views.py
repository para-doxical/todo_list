from django.shortcuts import render
from .models import Task, User


def homepage(request):
    """View for the homepage."""
    tasks = Task.objects.all()

    context = {'tasks' : tasks}
    return render(request, 'homepage.html', context)

def new_task(request):
    """View for new task page."""

    context = {}
    return render(request, 'new_task.html', context)

def task_page(request, pk):
    """View for task page."""
    task = Task.objects.get(pk=pk)

    context = {'task' : task}
    return render(request, 'task_page.html', context)