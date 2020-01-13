from django.shortcuts import render,HttpResponseRedirect
from app.models import Company,Programmer,Languages
from app.forms import ProgrammerForm

def company(request):
    cdata=Company.objects.all()
    return render(request,'app/index.html',context={'cdata':cdata})

def programmer(request):
    pdata=Programmer.objects.all()
    return render(request,'app/index.html',context={'pdata':pdata})

def languages(request):
    ldata=Languages.objects.all()
    return render(request,'app/index.html',context={'ldata':ldata})

def index(request):
    if request.method == "POST":
        form = ProgrammerForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/index/')
    else:
        form = ProgrammerForm()
        return render(request,'app/index.html',context={'form':form})
