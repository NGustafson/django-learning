from django.contrib import admin

from projects.models import Project
from .models import Task


# An Inline class to show the projects a task belongs to in the admin view
class TaskProjectsInline(admin.TabularInline):
    model = Project.tasks.through
    extra = 0


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']

    inlines = [TaskProjectsInline]
