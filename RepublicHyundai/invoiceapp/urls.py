from django.urls import path
from invoiceapp.views import preinvoiceview

urlpatterns = [

    path('preinvoice/',preinvoiceview),

]
