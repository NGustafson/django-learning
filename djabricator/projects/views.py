from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Project


class ProjectsList(ListView):
    model = Project
    context_object_name = 'projects'
    template_name = 'projects/list.html'


class ProjectsDetail(DetailView):
    model = Project
    context_object_name = 'project'
    template_name = 'projects/detail.html'
