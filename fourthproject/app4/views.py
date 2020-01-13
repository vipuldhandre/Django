from django.shortcuts import render

def submul(request):
    a,b=10,5
    c,d=1,2
    sub=a-b
    mul=c*d
    msg1="The substraction is:"
    msg2="The multiplication is:"
    dict1={'a':a,'b':b,'sub':sub}
    dict2={'c':c,'d':d,'mul':mul}
    return render(request,'app4/submul.html',context={'msg1':msg1,'msg2':msg2,'dict1':dict1,'dict2':dict2})

def sub(request):
    a,b=5,2
    sub=a-b
    msg="The substraction is:"
    dict={'a':a,'b':b,'sub':sub}
    return render(request,'app4/submul.html',context={'msg':msg,'dict':dict})

def mul(request):
    a,b=5,3
    mul=a*b
    msg="The multiplication is:"
    dict={'a':a,'b':b,'mul':mul}
    return render(request,'app4/submul.html',context={'msg':msg,'dict':dict})

    # Create your views here.
