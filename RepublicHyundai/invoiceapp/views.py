from django.shortcuts import render,HttpResponseRedirect
from servicesapp.models import *

def preinvoiceview(request):
    preinvoice = RoDetails.objects.all().last()
    print(preinvoice)
    return render(request,"invoiceapp/invoice.html",{'i':preinvoice})
