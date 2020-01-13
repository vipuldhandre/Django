from django.shortcuts import render
import datetime

def login(request):
    return render(request,'testapp/login.html')


def dict(request):
    name="vipul"
    education="BE(ENTC)"
    subject="M-I"
    marks=84
    address="Pune"
    college="BNCOE"
    data={'name':name,'education':education,'subject':subject,'marks':marks,'address':address,'college':college}
    return render(request,'testapp/dict.html',{'data':data})

def list(request):
    list=[{'name':'Vips','add':'Barcelona'},{'name':'Babya','add':'Liverpool'},{'name':'Kalya','add':'Madrid'},{'name':'Mangi','add':'Chelsy'}]
    #dict={'list':list}
    return render(request,'testapp/list.html',context={'list':list})

def dict2dict(request):
    dict2={'name':{1:'Vipul',2:'Vips'},'add':{1:'Pune',2:'Hinganghat'}}
    return render(request,'testapp/dict2.html',context={'dict2':dict2})

def list2dict(request):
    list2dict={'person1':[1,2,3,4,5,6],'person2':['a','b','c','d']}
    return render(request,'testapp/list2dict.html',context={'list2dict':list2dict})

def list2list(request):
    list2list=[['a','b','c','d'],[1,2,3,4]]
    return render(request,'testapp/list2list.html',context={'list2list':list2list})

def tupleintuple(request):
    tup=({1:2,3:4},{1:2})
    return render(request,'testapp/tuple.html',context={'tup':tup})

def setinset(request):
    setinset={[1,23,4],['a','b']}
    return render(request,'testapp/setinset.html',context={'setinset':setinset})

def date(request):
    d=datetime.datetime.now()
    msg="Hello Handsome! Good Morning!"
    return render(request,'testapp/date.html',context={"d":d,"msg":msg})
    # Create your views here.
