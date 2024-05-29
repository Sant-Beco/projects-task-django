from django.contrib import admin
from .models import project, Task, Estudiante, Actividades

# Register your models here.

admin.site.register(project)
admin.site.register(Task)
admin.site.register(Estudiante)
admin.site.register(Actividades)