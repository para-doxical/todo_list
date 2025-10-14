from django.shortcuts import render
from .models import Task, User


def homepage(request):
    """View for the homepage."""
    tasks = Task.objects.all()

    context = {'tasks' : tasks}
    return render(request, 'homepage.html', context)