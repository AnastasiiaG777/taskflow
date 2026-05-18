from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import (
    TaskListView,
    CreateTaskView,
    UpdateTaskView,
    DeleteTaskView,
    UserLoginView,
    UserRegisterView
)

urlpatterns = [
    path('', TaskListView.as_view(), name='tasks'),
    path('create/', CreateTaskView.as_view(), name='task_create'),
    path('update/<int:pk>/', UpdateTaskView.as_view(), name='task_update'),
    path('delete/<int:pk>/', DeleteTaskView.as_view(), name='task_delete'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', UserRegisterView.as_view(), name='register'),
]