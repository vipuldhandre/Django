from django.shortcuts import render,HttpResponseRedirect
from app.forms import TestForm
from django.views import View

class HomeView(View):
    form_class = TestForm
    template_name = "app/home.html"

    def get(self,request):
        form = self.form_class()
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/home/")
        return render(request,self.template_name,{'form':form})


# Create your views here.
