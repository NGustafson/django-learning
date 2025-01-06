from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ['name']
