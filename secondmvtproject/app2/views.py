from django.shortcuts import render
from .models import Book,Mobile


def book(request):
    msg="This is Book Table:"
    bookdata=Book.objects.all()
    return render(request,'app/bookdata.html',context={'msg':msg,'bookdata':bookdata})

def mobile(request):
    msg="This is Mobile Table:"
    mobiledata=Mobile.objects.all()
    return render(request,'app/mobdata.html',context={'msg':msg,'mobiledata':mobiledata})

def combine(request):
    msg1="This is Book Table:"
    msg2="This is Mobile Table:"
    bookdata=Book.objects.all()
    mobiledata=Mobile.objects.all()
    return render(request,'app/combine.html',context={'msg1':msg1,'msg2':msg2,'bookdata':bookdata,'mobiledata':mobiledata})
# Create your views here.
