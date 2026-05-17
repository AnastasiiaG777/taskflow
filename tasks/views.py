from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import TaskForm
from .models import Task
from django.urls import reverse_lazy
from django.db.models import Q


class TaskListView(ListView):
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'
    ordering = ['-created_at']
    paginate_by = 3

    def get_queryset(self):
        queryset = Task.objects.all().order_by('-created_at')

        search = self.request.GET.get('search')
        status = self.request.GET.get('status')

        if search:
            queryset = queryset.filter(
                Q(title__icontains=search) |
                Q(description__icontains=search)
            )

        if status:
            queryset = queryset.filter(status=status)

        return queryset


class CreateTaskView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_create.html'
    success_url = reverse_lazy('tasks')


class UpdateTaskView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_update.html'
    success_url = reverse_lazy('tasks')


class DeleteTaskView(DeleteView):
    model = Task
    template_name = 'tasks/task_delete.html'
    success_url = reverse_lazy('tasks')
