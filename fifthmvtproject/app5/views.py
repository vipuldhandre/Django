from django.shortcuts import render
from .models import Tester,Developer

def tester(request):
    msg="Tester Info:"
    testerdata=Tester.objects.filter(tname__iendswith="i")
    return render(request,'app/tester.html',context={'msg':msg,'testerdata':testerdata})


def developer(request):
    msg="Developer Info:"
    developerdata=Developer.objects.all()
    return render(request,'app/developer.html',context={'msg':msg,'developerdata':developerdata})

def combine(request):
    msg1="Tester Info:"
    msg2="Developer Info:"
    testerdata=Tester.objects.all()
    developerdata=Developer.objects.all()
    return render(request,'app/combine.html',context={'msg1':msg1,'msg2':msg2,'testerdata':testerdata,'developerdata':developerdata})


# Create your views here.
