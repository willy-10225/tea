from email import message
from django.shortcuts import get_object_or_404, redirect, render
from .models import Todo
from .forms import TodoForm
from datetime import datetime
from django.contrib.auth.decorators import login_required

# Create your views here.


video_parameter = {
        'text':
        '''  一、 材料與用水比例
（1）鮮品：水淹蓋過藥草材料為準。
（2）乾品：一兩藥材約600-800cc水。
二、煎煮藥材時間
（1）鮮品：先以強火煮沸，蓋上鍋蓋，再以煨火煎煮約30分鐘，熄火浸泡 約10分鐘，濾除藥材及雜質，取茶湯待用。
（2）乾品：先以強火煮沸，蓋上鍋蓋，再以煨火煎煮約60-80分鐘，熄火浸泡約10分鐘，濾除藥材及雜質，取茶湯待用。''',
        'height': '400px',
        'width': '100%',
        'src': '8223uFFnmvg',
        "date": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
video_parameter['textSplit']=video_parameter['text'].split('\n')

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
        todos = Todo.objects.all()

    return render(request, './todo/completed.html', {'todos': todos})


@login_required
def create(request):
    form = TodoForm()

    if request.method == 'POST':

        form = TodoForm(request.POST, request.FILES)
        todo = form.save(commit=False)
        todo.user = request.user
        todo.save()

        return redirect('todo')

    return render(request, './todo/create.html', {"form": form, "date": datetime.now().strftime('%Y-%m-%d %H:%M:%S')})


@login_required
def video(request):
    if request.method == 'POST':
        for i in [i for i in video_parameter.keys()][:-1]:
            if request.POST.get(f'{i}') is not '':
                video_parameter[f'{i}'] = request.POST.get(f'{i}')
                video_parameter['textSplit']=video_parameter['text'].split('\n')
    video_parameter.update({'message':'影片上傳成功','color':'success'})
    return render(request, './todo/video.html', video_parameter)


@login_required
def Resetvideo(request):
    return render(request, './todo/video.html', video_parameter)

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
    todos = Todo.objects.all()

    return render(request, './todo/todo.html', {'todos': todos})

def index(request):
    global video_parameter
    todos = Todo.objects.all()
    IndexList={'todos': todos}
    IndexList.update(video_parameter)

    return render(request, './todo/index.html', IndexList)