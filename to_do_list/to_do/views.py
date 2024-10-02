from django.shortcuts import render
from . models import Todolist

# Create your views here.
def todo(request):
    if request.POST :
        task=request.POST.get('task')
        deline=request.POST.get('deline')
        prio=request.POST.get('prio')

        todo_obj = Todolist(task=task,deline=deline,prio=prio)
        todo_obj.save()



    return render(request,'list.html')

def tasks(request):
    tasklist = Todolist.objects.all()
    return render(request,'task_list.html',{'tasks':tasklist})
