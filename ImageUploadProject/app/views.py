from django.shortcuts import render,HttpResponseRedirect
from app.forms import *
from app.models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

@login_required                  #decorator
def index(request):
    if request.method=='POST':
        form=ProfileForm(request.POST,request.FILES)
        print(request.POST)
        if form.is_valid():
            print(request.POST)
            form.save()
        return HttpResponseRedirect('/index/')

    else:
        form=ProfileForm()
        profiles = Profile.objects.all()
        return render(request,'app/index.html',context={'form':form,'profiles':profiles})

"""
class HomeView(LoginRequiredMixin,View):        #mixin
    template_name="app/index.html"
    #login_url='/login/'
    def get(self,request):
        return render(request,self.template_name)
"""
# Create your views here.
