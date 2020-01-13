from django.shortcuts import render,HttpResponseRedirect
from servicesapp.forms import LabourDetailsForm,LabourOperationMasterForm,RoDetailsForm,RoPartDetailsForm
from django.views import View

class LabourDetailsView(View):
    form_class = LabourDetailsForm
    template_name = "servicesapp/labourdetails.html"

    def get(self,request):
        form = self.form_class()
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/labourdetails/")
        return render(request,self.template_name,{'form':form})

class LabourOperationMasterView(View):
    form_class = LabourOperationMasterForm
    template_name = "servicesapp/labouroperationmaster.html"

    def get(self,request):
        form = self.form_class()
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/labouroperationmaster/")
        return render(request,self.template_name,{'form':form})

class RoDetailsView(View):
    form_class = RoDetailsForm
    template_name = "servicesapp/rodetails.html"

    def get(self,request):
        form = self.form_class()
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/rodetails/")
        return render(request,self.template_name,{'form':form})

class RoPartDetailsView(View):
    form_class = RoPartDetailsForm
    template_name = "servicesapp/ropartdetails.html"

    def get(self,request):
        form = self.form_class()
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/ropartdetails/")
        return render(request,self.template_name,{'form':form})

# Create your views here.
