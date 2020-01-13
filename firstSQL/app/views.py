from django.shortcuts import render
from .models import Student,Employee


def about(request):
    stuData=Student.objects.all()
    empData=Employee.objects.all()
    return render(request,'app/about.html',context={'stuData':stuData,'empData':empData})

def emp_data(request):
    empData=Employee.objects.all()
    return render(request,'app/employee.html',context={'empData':empData})


# Create your views here.
