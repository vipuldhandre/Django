from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login/')
def home(request):
    emp = Employee.objects.all()
    return render(request,'firstapp/home.html',context={'emp':emp})

@login_required(login_url='/login/')
def add(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            name = request.POST['ename']
            messages.success(request,f'Employee {name} added successfully.')

        return redirect('/home/')
    else:
        form = EmployeeForm()
        return render(request,'firstapp/add.html',context={'form':form})


@login_required(login_url="/login/")
def delete(request,id):
    emp = Employee.objects.get(pk=id)
    emp.delete()
    messages.info(request,f'Employee {emp.ename} deleted successfully.')
    return redirect('/home/')


@login_required(login_url="/login/")
def update(request,id):
    emp = Employee.objects.get(pk=id)
    form = EmployeeForm(instance = emp)
    if request.method == 'POST':
        form = EmployeeForm(request.POST,instance=emp)
        if form.is_valid():
            form.save()
            messages.info(request,f'Employee {emp.ename} updated successfully.')
        return redirect('/home/')
    else:
        return render(request,'firstapp/update.html',context={'form':form,'emp':emp})


# Create your views here.
