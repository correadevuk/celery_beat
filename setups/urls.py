from django.urls import path, include
from .views import register_task, result, edit_task, task_list

urlpatterns = [
    path('', register_task, name='settings'),
    path('edit_task/<int:task_id>', edit_task, name='edit_task'),
    path('task_list', task_list, name='task_list'),
    path('result', result, name='result')
]