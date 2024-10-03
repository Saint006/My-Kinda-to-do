from django.shortcuts import render
from . models import Todolist
from . forms import TaskForm

# Create your views here.
def todo(request):
    frm = TaskForm()
    if request.POST :
        frm=TaskForm(request.POST)
        if frm.is_valid:
            frm.save()
            frm=TaskForm
        else:
            frm=TaskForm()

    return render(request,'list.html',{'frm':frm})

def tasks(request):
    tasklist = Todolist.objects.all()
    return render(request,'task_list.html',{'tasks':tasklist})
