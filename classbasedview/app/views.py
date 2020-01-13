from django.shortcuts import render
from django.views import View

def home(request):
    msg="Welcome to class based view"
    return render(request,'app/index.html',context={'msg':msg})

class Homeview(View):
    def get(self,request,*var,**kvar):
        context=f' you entered {kvar} '
        print(var)
        for i in kvar:
            print(kvar[i])
        return render(request,'app/index.html',context={'context':context})



# Create your views here.
