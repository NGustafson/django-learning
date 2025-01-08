from django.urls import path

from . import views

app_name = 'tasks'
urlpatterns = [
    path('', views.TasksList.as_view(), name='tasks_list'),
    path('<pk>/', views.TaskDetail.as_view(), name='task_detail'),
]