from customerapp.models import (State,District,City,CustomerType,CustomerDetails)
from django.forms import ModelForm
from django import forms

class StateForm(ModelForm):
    class Meta:
        model = State
        fields = "__all__"

class DistrictForm(ModelForm):
    class Meta:
        model = District
        fields = "__all__"

class CityForm(ModelForm):
    class Meta:
        model = City
        fields = "__all__"

class CustomerTypeForm(ModelForm):
    class Meta:
        model = CustomerType
        fields = "__all__"

class CustomerDetailsForm(ModelForm):
    class Meta:
        model = CustomerDetails
        fields = "__all__"
        widgets = {
            "cust_dob":forms.DateInput(attrs={'type':'date'}),
        }
