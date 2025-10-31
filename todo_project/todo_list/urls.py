from django.urls import path, re_path
from .views import homepage, new_task, task_page

urlpatterns = [
    path('', homepage, name='homepage'),
    path('new/', new_task, name='new_task'),
    re_path(r"^task/(?P<pk>\d+)/$", task_page, name='task_page'),
 
]
