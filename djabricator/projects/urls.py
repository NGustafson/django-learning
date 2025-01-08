from django.urls import path

from . import views

app_name = 'projects'
urlpatterns = [
    path('', views.ProjectsList.as_view(), name='projects_list'),
    path('<pk>/', views.ProjectsDetail.as_view(), name='project_detail'),
    path('<int:project_id>/workboard/', views.project_workboard, name='project_workboard'),
]