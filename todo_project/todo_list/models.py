from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    # COMPLETED_STATUS = [
    #     ("Y", "Yes"),
    #     ("N", "NO")
    # ]
    title = models.CharField(max_length=256, unique=True)
    description = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(null=True, auto_now=True)
    is_completed = models.BooleanField(default=False)

    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='tasks')

