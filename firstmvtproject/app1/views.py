from django.shortcuts import render
from .models import Student,Employee

def Studata(request):
    msg="Student Information is:"
    studata=Student.objects.all()
    return render(request,'app/studata.html',context={'msg':msg,'studata':studata})

def Empdata(request):
    msg="Employee Information is:"
    empdata=Employee.objects.all()
    return render(request,'app/empdata.html',context={'msg':msg,'empdata':empdata})

def Combine(request):
    msg1="Student Information is:"
    msg2="Employee Information is:"
    empdata=Employee.objects.all()
    studata=Student.objects.all()
    return render(request,'app/combine.html',context={'msg1':msg1,'msg2':msg2,'studata':studata,'empdata':empdata})

# Create your views here.
