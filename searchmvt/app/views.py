from django.shortcuts import render
from app.models import Stusearch

def index(request):
    data1=Stusearch.objects.all()
    return render(request,'app/index.html',context={'data1':data1})

def search(request):
    print(request.GET)
    var=request.GET.get('stuname')  #request.GET['stuname']
    data=Stusearch.objects.filter(stuname__icontains=var)
    return render(request,'app/index.html',context={'data':data})


# Create your views here.
