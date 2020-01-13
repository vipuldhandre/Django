from django.forms import ModelForm
from vehicleapp.models import VehicleCategory,VehicleModel,VehicleDetails
from django import forms

class VehicleCategoryForm(ModelForm):
    class Meta:
        model = VehicleCategory
        fields = "__all__"

class VehicleModelForm(ModelForm):
    class Meta:
        model = VehicleModel
        fields = "__all__"

class VehicleDetailsForm(ModelForm):
    class Meta:
        model = VehicleDetails
        fields = "__all__"
        widgets = {
            "veh_reg_date":forms.DateInput(attrs={'type':'date'}),
        }
