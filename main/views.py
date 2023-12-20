from django.shortcuts import render

from .models import Task
from django.views.generic import DetailView


def index(request):
    tasks = Task.objects.all()
    data = {'title': 'Main page'}
    return render(request, 'task/index.html', {'title': 'Main page', 'tasks': tasks})



def about(request):
    return render(request, 'main/about.html')
