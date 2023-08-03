from django.shortcuts import render, redirect, get_object_or_404
from .forms import TodoForm
from .models import Todo

def index(request):
    todos = Todo.objects.all()
    context = {'form': TodoForm(), 'todos':todos}
    return render(request, 'index.html', context)


def add(request, id=None):
    pass         

def update(request,id):
    pass

def delete(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return redirect('index')