from django.shortcuts import render,HttpResponseRedirect
from orderapp.forms import OrderForm,OrderDetailsForm
from django.views import View

class OrderView(View):
    form_class = OrderForm
    template_name = "orderapp/order.html"

    def get(self,request):
        form = self.form_class()
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/order/")
        return render(request,self.template_name,{'form':form})

class OrderDetailsView(View):
    form_class = OrderDetailsForm
    template_name = "orderapp/orderdetails.html"

    def get(self,request):
        form = self.form_class()
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/orderdetails/")
        return render(request,self.template_name,{'form':form})



# Create your views here.
