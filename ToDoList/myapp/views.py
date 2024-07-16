from django.shortcuts import render
from .models import Task

def renderTask(request):
    tasks = Task.objects.all()
    return render(request,'index.html',{'tasks' : tasks})

def index(request):
    if request.method == 'POST':
        title = request.POST.get('add_task')
        description = request.POST.get('add_desc')
        task = Task(title=title,description=description)
        task.save()
        
        return render(request,'index.html')
    else:
        return render(request,'index.html')
    