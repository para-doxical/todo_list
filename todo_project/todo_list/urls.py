from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),

    path('new/', views.new_task, name='new_task'),

    path("task/<str:pk>/", views.task_page, name='task_page'),

    path('edit-task/<str:pk>/', views.edit_task, name='edit_task'),
 
]
