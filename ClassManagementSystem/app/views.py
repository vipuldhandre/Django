from django.shortcuts import render
from app.models import *
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    data=Student.objects.filter(sname__icontains="")
    return render(request,'app/index.html',context={'data':data})

def search(request):
    data=Student.objects.filter(sname__icontains=request.POST['key'])
    return render(request,'app/index.html',context={'data':data})

# Create your views here.
