from django.shortcuts import render, redirect
from .models import Task, User
from .forms import TaskForm

def homepage(request):
    """View for the homepage."""
    tasks = Task.objects.order_by('is_completed')

    context = {'tasks' : tasks}
    return render(request, 'todo_list/homepage.html', context)

def new_task(request):
    """View for new task page."""
    task_form = TaskForm()
    if request.method == 'POST':
        task_form = TaskForm(request.POST)
        if task_form.is_valid():
            created_task = task_form.save(commit=False)
            created_task.user = User.objects.first()
            created_task.save()
            return redirect('task_page', created_task.id)

    context = {'task_form' : task_form}
    return render(request, 'todo_list/new_task.html', context)

def task_page(request, pk):
    """View for task page."""
    task = Task.objects.get(pk=pk)

    context = {'task' : task}
    return render(request, 'todo_list/task_page.html', context)

def edit_task(request, pk):
    task = Task.objects.get(id=pk)
    task_form = TaskForm(instance=task)

    if request.method == 'POST':
        task_form = TaskForm(request.POST, instance=task)
        if task_form.is_valid():
            task_form.save()

            return redirect('task_page', pk)
    
    context = {'task_form' : task_form, 'task' : task}
    return render(request, 'todo_list/edit_task.html', context)