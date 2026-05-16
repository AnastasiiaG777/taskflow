from django.views.generic import ListView, CreateView
from .forms import TaskForm
from .models import Task
from django.urls import reverse_lazy


class TaskListView(ListView):
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'
    ordering = ['-created_at']
    paginate_by = 3


class CreateTaskView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_create.html'
    success_url = reverse_lazy('tasks')
