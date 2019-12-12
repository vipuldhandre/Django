from django.shortcuts import render,redirect
from .models import *


def home(request):
    emp = Employee.objects.all()
    return render(request,'firstapp/home.html',context={'emp':emp})


def add_employee(request):
    if request.method == "POST":
        print(request.POST)
        id = request.POST.get('key1')
        name = request.POST.get('key2')
        des = request.POST.get('key3')
        sal = request.POST.get('key4')
        Employee.objects.create(eid=id,ename=name,edes=des,esal=sal)
        return redirect('/home/')
    else:
        return render(request,'firstapp/add_employee.html')



def del_employee(request,eid):
    emp = Employee.objects.get(pk=eid)
    emp.delete()
    return redirect('/home/')


def update_employee(request,eid):
    emp = Employee.objects.get(pk=eid)
    return render(request,'firstapp/update_employee.html',context={'emp':emp})


def update_database(request):
    emp = Employee.objects.get(pk=request.POST.get('key1'))
    emp.ename = request.POST.get('key2')
    emp.edes = request.POST.get('key3')
    emp.esal = request.POST.get('key4')
    emp.save()
    return redirect('/home/')
# Create your views here.
