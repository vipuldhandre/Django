from django.shortcuts import render
from .models import Born,Human

def born(request):
    msg="Information of Human Being:"
    borndata=Born.objects.all()
    return render(request,'app/borndata.html',context={'msg':msg,'borndata':borndata})

def human(request):
    msg="Information of Human:"
    humandata=Human.objects.all()
    return render(request,'app/humandata.html',context={'msg':msg,'humandata':humandata})

def combine(request):
    msg1="Information of Human Being:"
    msg2="Information of Human:"
    borndata=Born.objects.all()
    humandata=Human.objects.all()
    return render(request,'app/combine.html',context={'msg1':msg1,'msg2':msg2,'borndata':borndata,'humandata':humandata})

# Create your views here.
