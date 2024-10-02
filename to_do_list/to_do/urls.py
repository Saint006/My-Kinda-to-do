from django.urls import path
from . import views

urlpatterns =[
     path('list/',views.todo,name='todo'),
     path('tasks/',views.tasks,name='task_list')
]