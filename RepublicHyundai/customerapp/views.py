from django.shortcuts import render,HttpResponseRedirect
from customerapp.forms import StateForm,DistrictForm,CityForm,CustomerDetailsForm
from django.views import View

class StateView(View):
    form_class = StateForm
    template_name = "customerapp/state.html"

    def get(self,request):
        form = self.form_class()
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/state/')
        return render(request,self.template_name,{'form':form})


class DistrictView(View):
    form_class = DistrictForm
    template_name = "customerapp/district.html"

    def get(self,request):
        form = self.form_class()
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/district/')
        return render(request,self.template_name,{'form':form})


class CityView(View):
    form_class = CityForm
    template_name = "customerapp/city.html"

    def get(self,request):
        form = self.form_class()
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/city/')
        return render(request,self.template_name,{'form':form})


class CustomerDetailsView(View):
    form_class = CustomerDetailsForm
    template_name = "customerapp/customerdetails.html"

    def get(self,request):
        form = self.form_class()
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/vehicledetails/')
        return render(request,self.template_name,{'form':form})
