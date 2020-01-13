from inventoryapp.models import ProductMaster,VendorDetails,ProductInventory
from django.forms import ModelForm
from django import forms

class ProductMasterForm(ModelForm):
    class Meta:
        model = ProductMaster
        fields = "__all__"

class VendorDetailsForm(ModelForm):
    class Meta:
        model = VendorDetails
        fields = "__all__"

class ProductInventoryForm(ModelForm):
    class Meta:
        model = ProductInventory
        fields = "__all__"
        widgets = {
            "prod_dispatch_date":forms.DateInput(attrs={'type':'date'}),
            "prod_received_date":forms.DateInput(attrs={'type':'date'}),
        }
