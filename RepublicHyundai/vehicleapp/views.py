from django.shortcuts import render,HttpResponseRedirect
from vehicleapp.forms import VehicleCategoryForm,VehicleModelForm,VehicleDetailsForm
from django.views import View

class VehicleCategoryView(View):
    form_class = VehicleCategoryForm
    template_name = "vehicleapp/vehiclecategory.html"

    def get(self,request):
        form = self.form_class()
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/vehiclecategory/")
        return render(request,self.template_name,{'form':form})

class VehicleModelView(View):
    form_class = VehicleModelForm
    template_name = "vehicleapp/vehiclemodel.html"

    def get(self,request):
        form = self.form_class()
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/vehiclemodel/")
        return render(request,self.template_name,{'form':form})

class VehicleDetailsView(View):
    form_class = VehicleDetailsForm
    template_name = "vehicleapp/vehicledetails.html"

    def get(self,request):
        form = self.form_class()
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/rodetails/")
        return render(request,self.template_name,{'form':form})


# Create your views here.
