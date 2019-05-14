from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Todo


def index(request):
    all_todos = Todo.objects.all()
    template = loader.get_template('todotracker/index.html')
    context = {
        'all_todos': all_todos,
    }
    return HttpResponse(template.render(context, request))

def add(request):
    all_todos = Todo.objects.all()
    template = loader.get_template('todotracker/add.html')
    context = {
        'all_todos': all_todos,
    }
    return HttpResponse(template.render(context, request))


def edit(request, todo_id):
    all_todos = Todo.objects.all()
    template = loader.get_template('todotracker/edit.html')
    context = {
        'all_todos': all_todos,
    }
    return HttpResponse(template.render(context, request))

def impressum(request):
    all_todos = Todo.objects.all()
    template = loader.get_template('todotracker/impressum.html')
    context = {
        'all_todos': all_todos,
    }
    return HttpResponse(template.render(context, request))
