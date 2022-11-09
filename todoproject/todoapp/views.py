from django.shortcuts import render, redirect
from . models import Task
from .form import TodoForm

# Create your views here.
def home(request):
    tasks = Task.objects.all()
    if request.method=='POST':
        name=request.POST.get('task','')
        priority=request.POST.get('priority','')
        date=request.POST.get('date','')
        time=request.POST.get('time','')
        task=Task(taskname=name,priority=priority,date=date,time=time)
        task.save()
    return render(request,'home.html',{'t':tasks})

def delete(request,taskid):
    task=Task.objects.get(id=taskid)
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    return render(request,'delete.html')

def update(request,taskid):
    task=Task.objects.get(id=taskid)
    form=TodoForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')

    return render(request,'update.html',{'f':form,'t':task})



