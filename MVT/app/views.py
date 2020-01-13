from django.shortcuts import render

def home(request,variable):
    msg=f'Hi i am {variable}'
    return render(request,'app/base.html',context={'msg':msg})

def home2(request):
    msg="Hi Vipul!"
    return render(request,'app/home2.html',context={'msg':msg})

def home3(request):
    msg="Hi Vipul!"
    return render(request,'app/home3.html',context={'msg':msg})

def home4(request):
    msg="Hi Vipul!"
    return render(request,'app/home4.html',context={'msg':msg})


# Create your views here.
