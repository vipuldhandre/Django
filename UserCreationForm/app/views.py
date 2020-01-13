from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from app.forms import RegistrationForm
from django.contrib import messages
def index(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/home/')
    else:
        form=UserCreationForm()
        return render(request,'app/home.html',{'form':form})

def home(request):
    if request.method=='POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username=request.POST['username']
            messages.success(request,f'User created successfully for user {username}')
        return HttpResponseRedirect('/home/')
    else:
        form=RegistrationForm()
        return render(request,'app/home.html',{'form':form})

# Create your views here.
