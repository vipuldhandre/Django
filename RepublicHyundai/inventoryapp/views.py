from django.shortcuts import render,HttpResponseRedirect
from inventoryapp.forms import ProductMasterForm,VendorDetailsForm,ProductInventoryForm
from django.views import View

class ProductMasterView(View):
    form_class = ProductMasterForm
    template_name = "inventoryapp/productmaster.html"

    def get(self,request):
        form = self.form_class()
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/productmaster/")
        return render(request,self.template_name,{'form':form})


class VendorDetailsView(View):
    form_class = VendorDetailsForm
    template_name = "inventoryapp/vendordetails.html"

    def get(self,request):
        form = self.form_class()
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/vendordetails/")
        return render(request,self.template_name,{'form':form})


class ProductInventoryView(View):
    form_class = ProductInventoryForm
    template_name = "inventoryapp/productinventory.html"

    def get(self,request):
        form = self.form_class()
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/productinventory/")
        return render(request,self.template_name,{'form':form})


# Create your views here.
