from django.db import models
from django.db.models import ManyToManyField

from tasks.models import Task


class Project(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(blank=True)
    tasks = ManyToManyField(Task, related_name='projects', blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'P{self.id}: {self.name}'


class Workboard(models.Model):
    project = models.OneToOneField(Project, on_delete=models.PROTECT)

    def __str__(self):
        return f"Workboard for {self.project.name}"

    def save(self, *args, **kwargs):
        is_new = self.pk is None
        super().save(*args, **kwargs)

        if is_new:
            default_column = Column.objects.create(
                workboard=self,
                name="Default",
                order=0
            )

            tasks = self.project.tasks.all()
            TaskColumnAssignment.objects.bulk_create([
                TaskColumnAssignment(task=task, column=default_column)
                for task in tasks
            ])


class Column(models.Model):
    workboard = models.ForeignKey(Workboard, related_name='columns', on_delete=models.PROTECT)
    name = models.CharField(max_length=200)
    # TODO: I would like the key  for this model to be (workboard, order), with order incrementing automatically
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f'Project: {self.workboard.project.name}, Column: {self.name}'


class TaskColumnAssignment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.PROTECT, null=False)
    column = models.ForeignKey(Column, on_delete=models.PROTECT, null=False)

    # Prevent tasks from being assigned to multiple columns in the same project
    def save(self, *args, **kwargs):
        if self.column.workboard:
            existing_assignment = (
                TaskColumnAssignment.objects.select_related('column__workboard').filter(
                    task=self.task,
                    column__workboard=self.column.workboard
                ).exclude(pk=self.pk))
            if existing_assignment.exists():
                raise ValueError(
                    f"Task '{self.task}' cannot be assigned to multiple columns on "
                    f"'{self.column.workboard}'"
                )
        super().save(*args, **kwargs)
