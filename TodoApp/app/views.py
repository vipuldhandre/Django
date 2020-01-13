from django.shortcuts import render,HttpResponseRedirect
from app.models import Todoapp

def index(request):
    tododata=Todoapp.objects.all()
    return render(request,'app/index.html',context={'tododata':tododata})

def addtodo(request):
    data=Todoapp.objects.get(key)
    data.save()
    print(request.POST)
    #return render(request,'app/home.html')
    return HttpResponseRedirect('/index/')

def deletetodo(request,todo_id):
    data=Todoapp.objects.get(pk=todo_id)
    data.delete()
    return HttpResponseRedirect('/index/')


# Create your views here.
