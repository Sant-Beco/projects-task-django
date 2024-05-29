from django.http import HttpResponse, JsonResponse
from .models import project, Task
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateNewTask, CreateNewProject

# Create your views here.

def index(request):
  return render(request, 'index.html')

def about(request):
  username = 'Santiago BedoYA Corra'
  return render(request, 'about.html', {
    'username': username
  })

def hello(request, username):
  print(username)
  return HttpResponse("<h1>Hello World</h1><p>Comienzos en django y python de santi</p><h3>Creado por %s</h3>"% username)

# def hello(request, id):
#   return HttpResponse("<h1>Hello World</h1><p>Comienzos en django y python de santi</p><h3>Creado por %s</h3>"% id)

def santi(request):
  return HttpResponse('<h2>Bienvenido a mi pagina la de santi</h2> <p>En este parte encontraras informacion muy relevante a que me dedico y que habilidades poseo</p>')

def projects(request):
  #projects = list(project.objects.values())
  projects = project.objects.all()
  return render(request, 'projects/projects.html',{
    'projects': projects
  })

def tasks(request):
  #task = Task.objects.get(title=title)
  tasks = Task.objects.all()
  return render(request, 'tasks/tasks.html',{
    'tasks': tasks
  })

# def create_task(request):
#   if request.method == 'GET':
#       return render(request, 'create_task.html',{
#         'form': CreateNewTask()
#     })
#   else:
#     Task.objects.create(title=request.POST['title'],description=request.POST['description'], project_id=2)
#     return redirect('/tasks/')


# Pruebas         # siur
  
def create_task(request):
  if request.method == 'GET':
      return render(request, 'tasks/create_task.html',{
        'form': CreateNewTask()
    })
  else:
    Task.objects.create(title=request.POST['title'],description=request.POST['description'], project_id=1)
    return redirect('tasks')
  
  # organizar no funciona correctamente 
def create_project(request):
  if request.method == 'GET':
    return render(request, 'projects/create_project.html', {
      'form': CreateNewProject()
    })
  else:
    project.objects.create(name=request.POST["name"])
    return redirect('projects')
    
    
def project_detail(request, id):
  project = get_object_or_404(project_id=id)
  print(project)
  return render(request, 'projects/detail.html', {
    'project': project
  })