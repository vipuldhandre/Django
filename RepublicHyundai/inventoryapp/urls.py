from django.urls import path
from inventoryapp.views import ProductMasterView,VendorDetailsView,ProductInventoryView


urlpatterns = [

    path('productmaster/',ProductMasterView.as_view()),
    path('vendordetails/',VendorDetailsView.as_view()),
    path('productinventory/',ProductInventoryView.as_view()),

]
