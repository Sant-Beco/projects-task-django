from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name="index"),
  path('about/', views.about, name="about"),
  path('santi/', views.santi, name="santi"),
  path('hello/<str:username>', views.hello, name="hello"),
  #path('hello/<int:id>', views.hello, name="")
  path('projects/', views.projects, name="projects"),
  path('projects/<int:id>', views.project_detail, name="project_detail"),
  path('tasks/', views.tasks, name="tasks"),
  path('create_task/', views.create_task, name="create_task"),
  path('create_project/', views.create_project, name="create_project")
]
