from django.shortcuts import render, redirect
from .models import Task

def index(request):
    if request.method == 'POST':
        title = request.POST.get('add_task')
        description = request.POST.get('add_desc')
        task = Task(title=title,description=description)
        task.save()
    else:
        tasks = Task.objects.all()
        count = tasks.count()
        return render(request,'index.html',{'tasks' : tasks, 'count' : count})
    
def removeTask(id):
    task = Task.objects.get(id=id)
    task.delete()
    print("done")
    return redirect('index')
    
    