from django.contrib import admin

from .models import Project, TaskColumnAssignment, Column, Workboard


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'description']
    prepopulated_fields = {'slug': ('name',)}


class TaskColumnAssignmentInline(admin.TabularInline):
    model = TaskColumnAssignment
    extra = 1
    readonly_fields = ['task', 'column']

    def get_queryset(self, request):
        """
        Modify the queryset to only show tasks for this column.
        """
        queryset = super().get_queryset(request)
        return queryset.select_related('task', 'column')


class ColumnInline(admin.StackedInline):
    model = Column
    extra = 1
    ordering = ['order']

    inlines = [TaskColumnAssignmentInline]


@admin.register(Workboard)
class WorkboardAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'project']
    search_fields = ['project__name']

    inlines = [ColumnInline]


@admin.register(TaskColumnAssignment)
class TaskColumnAssignmentAdmin(admin.ModelAdmin):
    list_display = ['task', 'column']