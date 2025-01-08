from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Task


class TasksList(ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'tasks/list.html'
    
    
class TaskDetail(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'tasks/detail.html'
    