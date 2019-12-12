from django.shortcuts import render,redirect
from .forms import *
from .models import *


def home(request):
    emp = Employee.objects.all()
    return render(request,'firstapp/home.html',context={'emp':emp})


def add(request):
    if request.method == "POST":
        print(request.POST)
        form = EmployeeForm(request.POST)
        Employee.objects.create(ename=request.POST['ename'],edes=request.POST['edes'],esal=request.POST['esal'])
        return redirect('/home/')
    else:
        form = EmployeeForm()
        return render(request,'firstapp/add.html',context={'form':form})


def delete(request,eid):
    emp = Employee.objects.get(pk=eid)
    emp.delete()
    return redirect('/home/')


def update(request,eid):
    emp = Employee.objects.get(pk=eid)
    initial = {'ename':emp.ename,'edes':emp.edes,'esal':emp.esal}
    form = EmployeeForm(initial=initial)
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            emp.ename = request.POST.get('ename')
            emp.edes = request.POST.get('edes')
            emp.esal = request.POST.get('esal')
            emp.save()
        return redirect('/home/')
    return render(request,'firstapp/update.html',context={'form':form,'emp':emp})


# Create your views here.
