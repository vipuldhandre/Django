from django.shortcuts import render,HttpResponseRedirect
from app.models import *
from app.forms import *

def index(request):
    if request.method=='POST':
        form=ProfileForm(request.POST,request.files)
        print(request.POST)
        if form.is_valid():
            print(request.POST)
            form.save()
        return HttpResponseRedirect('/home/')
    else:
        form=ProfileForm()
        profile=Profile.objects.all()
        return render(request,'app/home.html',context={'form':form,'profile':profile})



# Create your views here.
