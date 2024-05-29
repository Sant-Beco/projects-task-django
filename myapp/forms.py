from django import forms

# class CreateNewTask(forms.Form):
#   title = forms.CharField(label="Titulo de tarea", max_length=200)
#   description = forms.CharField(widget=forms.Textarea)


# Pruebas         # siu

class CreateNewTask(forms.Form):
  title = forms.CharField(label="Titulo de tarea", max_length=200, widget=forms.TextInput(attrs={'class': 'input'}))
  description = forms.CharField(widget=forms.Textarea(attrs={'class': 'input'}))

class CreateNewProject(forms.Form):
  name = forms.CharField(label="Nombre del proyecto", max_length=200, widget=forms.TextInput(attrs={'class': 'input'}))