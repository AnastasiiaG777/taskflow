from django.urls import path
from .views import TaskListView, CreateTaskView, UpdateTaskView

urlpatterns = [
    path('', TaskListView.as_view(), name='tasks'),
    path('create/', CreateTaskView.as_view(), name='task_create'),
    path('update/<int:pk>/', UpdateTaskView.as_view(), name='task_update'),
]