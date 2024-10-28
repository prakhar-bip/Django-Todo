from django.shortcuts import  get_object_or_404, redirect, render
from .models import Task
# Create your views here.
def Home(request):
    return render(request , 'Home.html')


def add_task(request):
    if request.method == "POST":
        title = request.POST['title']
        description = request.POST['task_desc']
        task = Task(Title=title, Description=description)
        task.save()
    
    return redirect('Home')
def view_tasks(request):
    tasks = Task.objects.all()
    return render(request, 'View_Tasks.html', {'tasks': tasks})


def delete_task(request, task_id):
    if(task_id):
        task = Task.objects.get(id=task_id)
        task.delete()
    else:
        raise "Task not found"

    return redirect('view')

def update_task(request, task_id):
    task = Task.objects.get(id = task_id)
    
    if request.method == "POST":
        title = request.POST['title']
        description = request.POST['task_desc']
        task.Title = title
        task.Description = description
        complete = request.POST['complete']
        if (complete == 'on'):
            task.Is_completed = True
            task.save()
            return redirect('view')
        else:
            task.save()
            return redirect('view')
    return render(request, 'Update.html', {'task': task})