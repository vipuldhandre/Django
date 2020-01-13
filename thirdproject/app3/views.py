from django.shortcuts import render

def set(request):
    msg="The Set is:"
    set={1,'a',2,'b',3,'c'}
    return render(request,'app3/set.html',context={'msg':msg,'set':set})

def alex(request):
    msg="I'm Alexandra! How Are you?"
    return render(request,'app3/alex.html',context={'msg':msg})

def addition(request):
    a,b=5,10
    sum=a+b
    dict={'a':a,'b':b,'sum':sum}
    msg="Addition of 2 number is:"
    return render(request,'app3/addition.html',context={'msg':msg,'dict':dict})
# Create your views here.
