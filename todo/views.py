from django.shortcuts import get_object_or_404, redirect, render
from .models import Todo
from .forms import TodoForm
from datetime import datetime
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    todos = Todo.objects.filter(completed=True)
    if request.user.is_authenticated:
        todos = Todo.objects.filter(user=request.user, completed=True)

    return render(request, './todo/index.html',{'todos': todos})

@login_required
def completed_by_id(request, id):
    todo = get_object_or_404(Todo, id=id)

    todo.completed = not todo.completed
    todo.date_completed = datetime.now() if todo.completed else None
    todo.save()

    return redirect('todo')


@login_required
def delete(request, id):
    todo = get_object_or_404(Todo, id=id)
    todo.delete()

    return redirect('todo')


@login_required
def completed(request):
    todos = None
    if request.user.is_authenticated:
        todos = Todo.objects.filter(user=request.user, completed=True)

    return render(request, './todo/completed.html', {'todos': todos})


@login_required
def create(request):
    message = ''
    form = TodoForm()

    if request.method == 'POST':
        message = '資料輸入錯誤'
        try:
            form = TodoForm(request.POST)
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()

            return redirect('todo')

        except Exception as e:
            print(e)

    return render(request, './todo/create.html', {'form': form, 'message': message})


@login_required
def view(request, id):
    message = ''
    todo = get_object_or_404(Todo, id=id)
    form = TodoForm(instance=todo)

    if request.method == 'POST':
        message = '更新錯誤!'

        if request.POST.get('delete'):
            todo.delete()
            return redirect('todo')

        if request.POST.get('update'):
            try:
                form = TodoForm(request.POST, instance=todo)
                if form.is_valid():
                    todo = form.save(commit=False)
                    todo.date_completed = datetime.now() if todo.completed else None
                    todo.save()

                    return redirect('todo')

            except Exception as e:
                print(e)

    return render(request, './todo/view.html', {'todo': todo, 'form': form, 'message': message})


def todo(request):
    todos = None
    if request.user.is_authenticated:
        todos = Todo.objects.filter(user=request.user)
        print(todos)

    return render(request, './todo/todo.html', {'todos': todos})