from django.shortcuts import render
from django.views.generic import ListView
from .models import Task


class TaskListView(ListView):
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'
    ordering = ['-created_at']
    paginate_by = 3

