from django.shortcuts import render
import datetime

def date(request):
    dt=datetime.datetime.now()
    msg="Hi Genteman, Today's Date and Time is:"
    return render(request,'testapp/date.html',context={'dt':dt,'msg':msg})

def list(request):
    msg="The list is:"
    list=[1,2,3,4]
    return render(request,'testapp/list.html',context={'msg':msg,'list':list})

def dict(request):
    msg="The dict is:"
    dict={'person1':{1:'vipul',2:'vips'},'person2':{1:'Babu',2:'Babya'}}
    return render(request,'testapp/dict.html',context={'msg':msg,'dict':dict})


# Create your views here.
