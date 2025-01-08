from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView

from .models import Project, Workboard, TaskColumnAssignment


def home_dashboard(request):
    return render(
        request,
        'dashboard/home.html'
    )


class ProjectsList(ListView):
    model = Project
    context_object_name = 'projects'
    template_name = 'projects/list.html'


class ProjectsDetail(DetailView):
    model = Project
    context_object_name = 'project'
    template_name = 'projects/detail.html'


def project_workboard(request, project_id):
    # Get current project or return 404 if the project doesn't exist
    project = get_object_or_404(Project, id=project_id)

    try:
        # Get workboard from project relation
        workboard = project.workboard
    except Workboard.DoesNotExist:
        # Redirect to the project detail page if the workboard doesn't exist.
        return redirect('projects:project_detail', project_id)


    # Columns for this workboard
    columns = workboard.columns.all()

    # Tasks for this project by column
    tasks_by_column = {}
    for column in columns:
        tasks = TaskColumnAssignment.objects.filter(column=column).select_related('task')
        tasks_by_column[column] = tasks

    return render(
        request,
        'projects/workboard.html',
        {
            'workboard': workboard,
            'columns': columns,
            'tasks_by_column': tasks_by_column}
    )
